import pathlib, urllib.request
BASE = pathlib.Path(__file__).parent / "public" / "images" / "products"
ITEMS = [
 ("body-splash-ayra", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/031440efc76d4396971d4f85b5d4ba76~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("vestido-suplex", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/733dbf7bcc6e4ab196bd8bf38fbb48b0~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("perfume-attrative", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/6a266919572044bc85f1d3bce2e4c20a~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("hidrabene-fps70", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/7ebce5ad4d614c519a4e64d0529a9a2a~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("cinta-modeladora", "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/a734cfcd190449f4bfc45773f19bae64~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("depilador-sobrancelha", "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/f5f40438e72143ba9348287a12c7a4c6~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("sutias-canelados", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/a5fb3ed197014be4b04bf20f540a2682~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("calcinhas-mirela", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/71e3683106194041a6a247e24b514000~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("jogo-toalhas", "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/de8b169255ff40e4bb27fb2cda5dccc2~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("blusa-gola-boba", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/37c92749f79e45fdb337fee5f5ce08e5~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("bolsas-baguete", "https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/2e7de48ba0884ff4ab371495d91c7233~tplv-aphluv4xwc-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
 ("baby-doll", "https://p16-oec-va.ibyteimg.com/tos-maliva-i-o3syd03w52-us/8b14b694f4f24877bf7c98e9b3385632~tplv-o3syd03w52-resize-jpeg:800:800.jpeg?dr=15584&t=555f072d&ps=933b5bde&shp=2408c917&shcp=32ce9e9e&idc=my2&from=604555543"),
]
ok, fail = 0, []
for slug, url in ITEMS:
    d = BASE / slug
    d.mkdir(parents=True, exist_ok=True)
    dest = d / "cover.jpg"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126", "Referer": "https://shop.tiktok.com/"})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, "wb") as f:
            f.write(r.read())
        print("OK", slug, dest.stat().st_size)
        ok += 1
    except Exception as e:
        print("FAIL", slug, str(e)[:150])
        fail += 1
print(f"done ok={ok} fail={fail}")
