#!/usr/bin/env python3
"""Validate SniffleShop as a current AltSource with SideStore compatibility."""
from __future__ import annotations
import argparse, json, re, sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

SOURCE_REQUIRED={"name","apps"}
SOURCE_ALLOWED=SOURCE_REQUIRED|{"identifier","sourceURL","subtitle","description","iconURL","headerURL","website","fediUsername","patreonURL","tintColor","nsfw","featuredApps","news"}
APP_REQUIRED={"name","bundleIdentifier","developerName","localizedDescription","iconURL","versions"}
APP_ALLOWED=APP_REQUIRED|{"beta","subtitle","tintColor","category","screenshots","screenshotURLs","appPermissions","permissions","version","versionDate","versionDescription","downloadURL","size"}
VERSION_REQUIRED={"version","date","downloadURL","size"}
VERSION_ALLOWED=VERSION_REQUIRED|{"buildVersion","marketingVersion","localizedDescription","minOSVersion","maxOSVersion","sha256"}
PERMISSION_TYPES={"photos","camera","location","contacts","reminders","music","microphone","speech-recognition","background-audio","background-fetch","bluetooth","network","calendars","faceid","siri","motion"}
CATEGORIES={"developer","entertainment","games","lifestyle","other","photo-video","social","utilities"}
NEWS_REQUIRED={"title","identifier","caption","date"}
NEWS_ALLOWED=NEWS_REQUIRED|{"appID","imageURL","notify","tintColor","url"}
class ValidationError(Exception): pass

def fail(path,msg): raise ValidationError(f"{path}: {msg}")
def obj(v,p):
    if not isinstance(v,dict): fail(p,"must be an object")
    return v
def string(v,p,nonempty=True):
    if not isinstance(v,str): fail(p,"must be a string")
    if nonempty and not v.strip(): fail(p,"must not be empty")
    return v
def keys(o,p,req,allowed):
    missing=sorted(req-o.keys()); extra=sorted(o.keys()-allowed)
    if missing: fail(p,f"missing required key(s): {', '.join(missing)}")
    if extra: fail(p,f"unsupported/unreviewed key(s): {', '.join(extra)}")
def https(v,p):
    q=urlparse(string(v,p))
    if q.scheme!="https" or not q.netloc: fail(p,"must be an absolute HTTPS URL")
def tint(v,p):
    if not re.fullmatch(r"#?[0-9A-Fa-f]{6}",string(v,p)): fail(p,"must be a 6-digit hexadecimal color")
def date(v,p):
    s=string(v,p)
    try: return datetime.fromisoformat(s.replace("Z","+00:00"))
    except ValueError: fail(p,f"invalid ISO-8601 date: {s!r}")

def screenshot(v,p):
    if isinstance(v,str): return https(v,p)
    o=obj(v,p); keys(o,p,{"imageURL"},{"imageURL","width","height"}); https(o["imageURL"],p+".imageURL")
    for k in ("width","height"):
        if k in o and (isinstance(o[k],bool) or not isinstance(o[k],(int,float)) or o[k]<=0): fail(p+"."+k,"must be positive")
def screenshots(v,p):
    if isinstance(v,list):
        for i,x in enumerate(v): screenshot(x,f"{p}[{i}]")
        return
    o=obj(v,p); allowed={"iphone","ipad","iphone-standard","iphone-edgeToEdge"}
    if o.keys()-allowed: fail(p,"unsupported screenshot group")
    for g,items in o.items():
        if not isinstance(items,list): fail(f"{p}.{g}","must be an array")
        for i,x in enumerate(items): screenshot(x,f"{p}.{g}[{i}]")
def app_permissions(v,p):
    o=obj(v,p)
    if o.keys()-{"entitlements","privacy"}: fail(p,"unsupported appPermissions key")
    if "entitlements" in o:
        if not isinstance(o["entitlements"],list): fail(p+".entitlements","must be an array")
        for i,x in enumerate(o["entitlements"]): string(x,f"{p}.entitlements[{i}]")
        if len(o["entitlements"])!=len(set(o["entitlements"])): fail(p+".entitlements","contains duplicates")
    if "privacy" in o:
        q=obj(o["privacy"],p+".privacy")
        for k,v in q.items(): string(k,p+".privacy key"); string(v,p+".privacy."+k)
def version(v,p):
    o=obj(v,p); keys(o,p,VERSION_REQUIRED,VERSION_ALLOWED); string(o["version"],p+".version"); d=date(o["date"],p+".date"); https(o["downloadURL"],p+".downloadURL")
    if isinstance(o["size"],bool) or not isinstance(o["size"],(int,float)) or o["size"]<=0: fail(p+".size","must be a positive number of bytes")
    for k in ("buildVersion","marketingVersion","localizedDescription","minOSVersion","maxOSVersion"):
        if k in o: string(o[k],p+"."+k,nonempty=k!="localizedDescription")
    if "sha256" in o and not re.fullmatch(r"[0-9a-fA-F]{64}",string(o["sha256"],p+".sha256")): fail(p+".sha256","must be 64 hex characters")
    return d
def app(a,i):
    p=f"apps[{i}]"; o=obj(a,p); keys(o,p,APP_REQUIRED,APP_ALLOWED)
    for k in ("name","bundleIdentifier","developerName","localizedDescription"): string(o[k],p+"."+k)
    https(o["iconURL"],p+".iconURL")
    if "beta" in o and not isinstance(o["beta"],bool): fail(p+".beta","must be boolean")
    if "subtitle" in o: string(o["subtitle"],p+".subtitle")
    if "tintColor" in o: tint(o["tintColor"],p+".tintColor")
    if "category" in o and string(o["category"],p+".category") not in CATEGORIES: fail(p+".category","unsupported category")
    if "screenshots" in o: screenshots(o["screenshots"],p+".screenshots")
    su=o.get("screenshotURLs",[])
    if not isinstance(su,list): fail(p+".screenshotURLs","must be an array")
    for j,u in enumerate(su): https(u,f"{p}.screenshotURLs[{j}]")
    if "appPermissions" in o: app_permissions(o["appPermissions"],p+".appPermissions")
    perms=o.get("permissions",[])
    if not isinstance(perms,list): fail(p+".permissions","must be an array")
    for j,x in enumerate(perms):
        q=f"{p}.permissions[{j}]"; x=obj(x,q); keys(x,q,{"type","usageDescription"},{"type","usageDescription"})
        if string(x["type"],q+".type") not in PERMISSION_TYPES: fail(q+".type","unsupported SideStore permission type")
        string(x["usageDescription"],q+".usageDescription")
    vs=o["versions"]
    if not isinstance(vs,list) or not vs: fail(p+".versions","must be a non-empty array")
    ds=[version(v,f"{p}.versions[{j}]") for j,v in enumerate(vs)]
    aware=[d.tzinfo is not None for d in ds]
    if all(aware) or not any(aware):
        for j in range(len(ds)-1):
            if ds[j]<ds[j+1]: fail(p+".versions","must be newest-first")
    return o["bundleIdentifier"]
def validate(data):
    o=obj(data,"$"); keys(o,"$",SOURCE_REQUIRED,SOURCE_ALLOWED); string(o["name"],"$.name")
    if "identifier" in o: string(o["identifier"],"$.identifier")
    for k in ("sourceURL","iconURL","headerURL","website","patreonURL"):
        if k in o: https(o[k],"$."+k)
    for k in ("subtitle","description","fediUsername"):
        if k in o: string(o[k],"$."+k)
    if "tintColor" in o: tint(o["tintColor"],"$.tintColor")
    if "nsfw" in o and not isinstance(o["nsfw"],bool): fail("$.nsfw","must be boolean")
    if not isinstance(o["apps"],list) or not o["apps"]: fail("$.apps","must be a non-empty array")
    ids=set(); names=set()
    for i,a in enumerate(o["apps"]):
        bid=app(a,i)
        if bid in ids: fail(f"apps[{i}].bundleIdentifier","duplicate")
        ids.add(bid); n=a["name"].casefold()
        if n in names: fail(f"apps[{i}].name","duplicate")
        names.add(n)
    featured=o.get("featuredApps",[])
    if not isinstance(featured,list) or len(featured)>5: fail("$.featuredApps","must be an array of at most five bundle IDs")
    for i,b in enumerate(featured):
        if string(b,f"$.featuredApps[{i}]") not in ids: fail(f"$.featuredApps[{i}]","does not match an app")
    news=o.get("news",[])
    if not isinstance(news,list): fail("$.news","must be an array")
    seen=set()
    for i,n in enumerate(news):
        p=f"news[{i}]"; n=obj(n,p); keys(n,p,NEWS_REQUIRED,NEWS_ALLOWED)
        for k in NEWS_REQUIRED: string(n[k],p+"."+k)
        date(n["date"],p+".date")
        for k in ("imageURL","url"):
            if k in n: https(n[k],p+"."+k)
        if "appID" in n and n["appID"] not in ids: fail(p+".appID","does not match an app")
        if n["identifier"] in seen: fail(p+".identifier","duplicate")
        seen.add(n["identifier"])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("source",nargs="?",default="source.json"); args=ap.parse_args(); path=Path(args.source)
    try: data=json.loads(path.read_text(encoding="utf-8")); validate(data)
    except (OSError,json.JSONDecodeError,ValidationError) as exc: print(f"FAIL: {exc}",file=sys.stderr); return 1
    print(f"OK: {path} is a valid reviewed AltSource/SideStore source ({len(data['apps'])} apps)"); return 0
if __name__=="__main__": raise SystemExit(main())
