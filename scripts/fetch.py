import json, os, re, sys, time, urllib.request, urllib.error

OUT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(OUT, "files")
os.makedirs(RAW, exist_ok=True)

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36")

def fetch(url, name, referer=None):
    dest = os.path.join(RAW, name)
    if os.path.exists(dest) and os.path.getsize(dest) > 2000:
        return classify(dest, name, url, cached=True)
    hdrs = {"User-Agent": UA,
            "Accept": "application/pdf,application/octet-stream,*/*",
            "Accept-Language": "en-US,en;q=0.9"}
    if referer:
        hdrs["Referer"] = referer
    req = urllib.request.Request(url, headers=hdrs)
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            data = r.read()
            ctype = r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        return (name, "HTTP %s" % e.code, url, 0, 0)
    except Exception as e:
        return (name, "ERR %s" % type(e).__name__, url, 0, 0)
    if not data.startswith(b"%PDF"):
        head = data[:120].decode("latin-1", "ignore").replace("\n", " ")
        return (name, "NOT-PDF(%s) %s" % (ctype[:30], head[:60]), url, len(data), 0)
    open(dest, "wb").write(data)
    return classify(dest, name, url, cached=False)

def classify(dest, name, url, cached=False):
    b = open(dest, "rb").read()
    pages = len(re.findall(rb"/Type\s*/Page[^s]", b))
    if pages == 0:
        pages = len(re.findall(rb"/Count\s+(\d+)", b)) and 0
    return (name, "OK" + (" cache" if cached else ""), url, len(b), pages)

urls = json.load(open(os.path.join(OUT, "urls.json"), encoding="utf-8"))
rows = []
for item in urls:
    rows.append(fetch(item["u"], item["n"], item.get("r")))
    time.sleep(0.4)

print("%-30s %-8s %8s %6s  %s" % ("FILE", "STATUS", "BYTES", "PAGES", "SOURCE"))
print("-" * 118)
for n, st, u, ln, pg in rows:
    print("%-30s %-8s %8d %6d  %s" % (n[:30], st[:8], ln, pg, u[:70]))
ok = [r for r in rows if r[1].startswith("OK")]
print("\n%d/%d downloaded as valid PDF" % (len(ok), len(rows)))
