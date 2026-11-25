#!/usr/bin/env python3
"""Fase (a), passo 5: fotos da PJ Comercial (fonte extra de imagens).

Lê raw/pj/html/*.html (baixados de pjcomercial.com.br), extrai as fotos de
cada produto da loja e associa ao produto da PLAS correspondente.
Só associa automaticamente quando o slug antigo ou o nome batem exatamente;
quando há homônimos, desempata pelas medidas da descrição. O resto vai para
data/pj-products.json com match=None e entra no PENDENCIAS.md.

Saída: data/pj-products.json, data/pj-images-manifest.json
"""
import glob
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def norm(s):
    s = html.unescape(s).replace("×", "x")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def main():
    plas = json.load(open(ROOT / "data/products.json"))
    by_old = {p["oldSlug"]: p for p in plas}
    by_name = {}
    for p in plas:
        by_name.setdefault(norm(p["oldName"]), []).append(p)

    out = []
    for f in sorted(glob.glob(str(ROOT / "raw/pj/html/*.html"))):
        s = html.unescape(open(f, encoding="utf-8").read())
        i = s.find('"productData":[0,{')
        if i < 0:
            continue
        blk = s[i:s.find('"additional_info"', i)]
        title = re.search(r'"title":\[0,"([^"]*)"', blk).group(1)
        slug = re.search(r'"slug":\[0,"([^"]*)"', blk).group(1)
        d = re.search(r'"description":\[0,"(.*?)"\],"thumbnail"', blk, re.S)
        desc = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", d.group(1))) if d else ""
        imgs = re.findall(r'"url":\[0,"(https://cdn\.zyrosite\.com/cdn-ecommerce/[^"]+)"\]', blk)

        match, how = None, None
        cands = by_name.get(norm(title), [])
        if len(cands) > 1:  # homônimos: desempata pela medida interna citada na descrição
            for c in cands:
                internal = (c["dimensions"].get("internal") or {}).get("raw", "")
                if internal and internal.split(" cm")[0] in desc:
                    match, how = c, "nome+medidas"
        elif len(cands) == 1:
            match, how = cands[0], "nome"
        if not match and slug in by_old:
            match, how = by_old[slug], "slug"
        out.append({"pjSlug": slug, "pjTitle": title, "pjDesc": desc, "images": imgs,
                    "match": match["slug"] if match else None, "how": how})

    # nomes de arquivo: pj/<slug-plas>[-n].ext ou pj/sem-associacao/<slug-pj>[-n].ext
    manifest, used = [], {}
    for o in out:
        base = o["match"] or f"sem-associacao/{o['pjSlug']}"
        for url in o["images"]:
            ext = url.rsplit(".", 1)[1].lower().replace("jpeg", "jpg")
            used[base] = used.get(base, 0) + 1
            name = base if used[base] == 1 else f"{base}-{used[base]}"
            manifest.append({"url": url, "file": f"pj/{name}.{ext}", "product": o["match"], "pjSlug": o["pjSlug"]})
    # imagens de conteúdo (banners, catálogo) em assets.zyrosite.com.
    # O link original é o mesmo sem o trecho cdn-cgi/image/...
    pat = re.compile(r"https://assets\.zyrosite\.com/(?:cdn-cgi/image/[^/]+/)?([A-Za-z0-9]+/[A-Za-z0-9._-]+\.(?:png|jpe?g|webp|gif|avif))", re.I)
    seen_on = {}
    for f in sorted(glob.glob(str(ROOT / "raw/pj/html/*.html"))):
        page = Path(f).stem
        for k in set(pat.findall(open(f, encoding="utf-8", errors="ignore").read())):
            seen_on.setdefault(k, []).append(page)
    n = 0
    for k, pages in sorted(seen_on.items()):
        if len(pages) > 10 or "logo" in k.lower():  # logo/ícones repetidos em todas as páginas
            continue
        n += 1
        ext = k.rsplit(".", 1)[1].lower().replace("jpeg", "jpg")
        manifest.append({"url": f"https://assets.zyrosite.com/{k}", "file": f"pj/conteudo/{pages[0]}-{n}.{ext}",
                         "product": None, "pjSlug": pages[0]})

    json.dump(out, open(ROOT / "data/pj-products.json", "w"), ensure_ascii=False, indent=1)
    json.dump(manifest, open(ROOT / "data/pj-images-manifest.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(out)} produtos PJ, {sum(1 for o in out if o['match'])} associados, {len(manifest)} imagens")
    for o in out:
        if not o["match"]:
            print("  sem associação:", o["pjTitle"], f"({o['pjSlug']})")


if __name__ == "__main__":
    main()
