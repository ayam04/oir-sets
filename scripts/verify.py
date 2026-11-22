import glob, os, re, zlib

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")

def streams(b):
    for m in re.finditer(rb"stream\r?\n", b):
        s = m.end(); e = b.find(b"endstream", s)
        if e < 0:
            continue
        raw = b[s:e]
        for c in (raw, raw.rstrip(b"\r\n")):
            try:
                yield zlib.decompress(c); break
            except Exception:
                continue

def pages(b):
    n = len(re.findall(rb"/Type\s*/Page[^s]", b))
    if n:
        return n
    for d in streams(b):
        c = len(re.findall(rb"/Type\s*/Page[^s]", d))
        if c:
            n = max(n, c)
    if n == 0:
        m = re.search(rb"/Pages\b.{0,400}?/Count\s+(\d+)", b, re.S)
        if m:
            n = int(m.group(1))
    return n

def nimg(b):
    return len(re.findall(rb"/Subtype\s*/Image", b))

def txt(b):
    out = []
    for d in streams(b):
        if b"BT" not in d:
            continue
        for t in re.finditer(rb"\(((?:\\.|[^\\()])*)\)", d):
            out.append(t.group(1).decode("latin-1", "ignore"))
    return re.sub(r"\s+", " ", " ".join(out)).strip()

print("%-40s %8s %5s %5s  %s" % ("FILE", "BYTES", "PGS", "IMGS", "TEXT SAMPLE"))
print("-" * 132)
for p in sorted(glob.glob(os.path.join(RAW, "*.pdf"))):
    b = open(p, "rb").read()
    t = txt(b)
    print("%-40s %8d %5d %5d  %s" % (os.path.basename(p)[:40], len(b), pages(b), nimg(b), t[:60]))
