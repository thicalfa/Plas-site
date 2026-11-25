#!/usr/bin/env python3
"""Fase (a): converte o JSON bruto da loja antiga em data/products.json.

Entrada: raw/products-*.json (API WooCommerce Store, baixada por scripts/fetch.sh)
Saída:   data/products.json, data/categories.json, data/redirects.json,
         data/images-manifest.json, data/issues.json (lido por scripts/pendencias.py)

Regra do briefing: nunca inventar dados. Todo valor numérico vem do texto
original; o texto original de cada linha fica guardado em `specs`.
"""
import glob
import html
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = sorted(glob.glob(str(ROOT / "raw/products-*.json")))
OUT = ROOT / "data"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- categorias
# Estrutura nova (slugs em português, sem erros de digitação do site antigo).
CATEGORIES = [
    ("caixas-plasticas", "Caixas plásticas", [
        ("caixas-vazadas", "Caixas vazadas"),
        ("caixas-fechadas", "Caixas fechadas"),
        ("caixas-klt", "Caixas KLT"),
    ]),
    ("bandejas", "Bandejas", []),
    ("lixeiras", "Lixeiras", [
        ("coleta-seletiva", "Coleta seletiva"),
        ("lixeiras-com-pedal", "Lixeiras com pedal"),
        ("lixeiras-basculantes", "Lixeiras basculantes"),
        ("lixeiras-plasticas", "Lixeiras plásticas"),
    ]),
    ("pallets", "Pallets", [
        ("pallets-plasticos", "Pallets plásticos"),
        ("pallets-de-contencao", "Pallets de contenção"),
        ("pallets-rotomoldados", "Pallets rotomoldados"),
    ]),
    ("containers-e-carros", "Containers e carros", [
        ("carrinhos-de-limpeza", "Carrinhos de limpeza"),
    ]),
    ("estrados", "Estrados", []),
    ("cestos-e-gaveteiros", "Cestos e gaveteiros", [
        ("cestos", "Cestos"),
        ("gaveteiros", "Gaveteiros"),
    ]),
    ("moveis-plasticos", "Móveis plásticos", [
        ("cadeiras", "Cadeiras"),
        ("mesas", "Mesas"),
        ("espreguicadeiras", "Espreguiçadeiras"),
        ("banquetas", "Banquetas"),
    ]),
]

# slug antigo -> (categoria nova, subcategoria nova ou None)
OLD_CAT = {
    "caixas-plasticas": ("caixas-plasticas", None),
    "caixas-vazadas": ("caixas-plasticas", "caixas-vazadas"),
    "caixas-fechadas": ("caixas-plasticas", "caixas-fechadas"),
    "caixas-klt": ("caixas-plasticas", "caixas-klt"),
    "bandejas": ("bandejas", None),
    "lixeiras": ("lixeiras", None),
    "coleta-seletiva": ("lixeiras", "coleta-seletiva"),
    "lixeiras-com-pedal": ("lixeiras", "lixeiras-com-pedal"),
    "lixeiras-basculante": ("lixeiras", "lixeiras-basculantes"),
    "lixeiras-plastica": ("lixeiras", "lixeiras-plasticas"),
    "pallets": ("pallets", None),
    "pallets-plastico": ("pallets", "pallets-plasticos"),
    "pallets-contencao": ("pallets", "pallets-de-contencao"),
    "pallets-rotomodaldo": ("pallets", "pallets-rotomoldados"),
    "containners-e-carros": ("containers-e-carros", None),
    "carrinho-de-limpeza": ("containers-e-carros", "carrinhos-de-limpeza"),
    "estrados": ("estrados", None),
    "cestos-e-gaveteiros": ("cestos-e-gaveteiros", None),
    "cestos": ("cestos-e-gaveteiros", "cestos"),
    "gaveteiros": ("cestos-e-gaveteiros", "gaveteiros"),
    "moveis-plasticos": ("moveis-plasticos", None),
    "cadeiras": ("moveis-plasticos", "cadeiras"),
    "mesas": ("moveis-plasticos", "mesas"),
    "espreguicadeiras": ("moveis-plasticos", "espreguicadeiras"),
    "banquetas": ("moveis-plasticos", "banquetas"),
}
# Quando um produto está em duas subcategorias, a mais específica vence.
SUB_PRIORITY = ["caixas-klt"]

# Produtos "Uncategorized" no site antigo: categoria provisória (confirmar).
UNCATEGORIZED_GUESS = {
    "banco-de-plastico-comfort-com-encosto": ("moveis-plasticos", "banquetas"),
    "caixa-fechada-50-litros": ("caixas-plasticas", "caixas-fechadas"),
    "caixa-fechada-74-litros": ("caixas-plasticas", "caixas-fechadas"),
    "mesa-plastica-retangular": ("moveis-plasticos", "mesas"),
    "pa-plastica-com-cabo-e-tampa-plastica": ("containers-e-carros", "carrinhos-de-limpeza"),
}

issues = []  # {slug, name, kind, detail}

# Produtos com o mesmo nome no site antigo: nome de exibição derivado dos
# próprios dados (capacidade/medida), para o cliente distinguir. Confirmar.
DISPLAY_NAME = {
    "cesto-de-pao": "Cesto de Pão 40 litros",
    "cesto-de-pao-2": "Cesto de Pão 51 litros",
    "caixa-fechada-130-litros": "Caixa Fechada 130 litros (40,5 x 55,5 x 76 cm)",
    "caixa-fechada-130-litros-2": "Caixa Fechada 130 litros (41 x 56 x 78 cm)",
}
NEW_SLUG = {
    "cesto-de-pao": "cesto-de-pao-40-litros",
    "cesto-de-pao-2": "cesto-de-pao-51-litros",
    "caixa-fechada-130-litros": "caixa-fechada-130-litros-76",
    "caixa-fechada-130-litros-2": "caixa-fechada-130-litros-78",
    "estrado-1060": "estrado-1060",
}


def issue(p, kind, detail):
    issues.append({"slug": p["slug"], "name": p["name"], "kind": kind, "detail": detail})


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-+", "-", s)


def clean_name(n):
    """Só correções de forma (entidades HTML, espaços, abreviações, digitação)."""
    n = html.unescape(n)
    n = re.sub(r"\s+", " ", n).strip()
    n = re.sub(r"\bc/\s*", "com ", n, flags=re.I)
    n = n.replace("Rotomoldado100", "Rotomoldada 100").replace("baculante", "basculante")
    n = n.replace("Plásticos 1000", "Plástico 1000")
    n = re.sub(r"(\d)\s*×\s*(\d)", r"\1x\2", n)
    n = re.sub(r"^Lixeira com tampa vai vem 100 litros$", "Lixeira 100 litros com tampa vai e vem", n)
    n = re.sub(r"tampa vai vem", "tampa vai e vem", n)
    n = re.sub(r"(\d+) [Ll]itros\b", r"\1 litros", n)
    return n[0].upper() + n[1:]


def num(s):
    """'1.500' -> 1500, '0,992' -> 0.992, '3.000,5' -> 3000.5. None se ambíguo."""
    s = s.strip()
    if re.fullmatch(r"\d{1,3}(\.\d{3})+(,\d+)?", s):
        return float(s.replace(".", "").replace(",", "."))
    if re.fullmatch(r"\d+(,\d+)?", s):
        return float(s.replace(",", "."))
    if re.fullmatch(r"\d+\.\d+", s):  # ponto decimal (ex.: 4.5) – ambíguo
        return None
    return None


def parse_dims(p, label, value):
    """'15,0 x 22,5 x 51,0 cm.' -> {raw, cm:[...], unit}"""
    raw = value.strip().rstrip(".")
    unit = "cm" if re.search(r"\bcm\b", raw, re.I) else ("mm" if re.search(r"\bmm\b", raw, re.I) else None)
    body = re.sub(r"\s*(cm|mm)\.?\s*$", "", raw, flags=re.I)
    parts = re.split(r"\s*[x×]\s*", body)
    vals, ok = [], True
    for part in parts:
        v = num(part)
        if v is None:
            ok = False
            break
        vals.append(v)
    if ok and len(vals) == 1:
        issue(p, "medida-sem-unidade", f"{label}: \"{raw}\" é um número só, sem unidade")
        return {"raw": raw, "cm": None, "unit": unit}
    if not ok or not (2 <= len(vals) <= 3):
        probable = None
        fixed = re.sub(r"(\d+,\d+),0\b", r"\1", body)      # 15,5,0 -> 15,5
        fixed = re.sub(r",\s*(?=[x×])", " ", fixed)            # 82,0, x -> 82,0 x
        pv = [num(x) for x in re.split(r"\s*[x×]\s*", fixed)]
        if all(v is not None for v in pv) and 2 <= len(pv) <= 3:
            probable = pv
        hint = f" (provável: {' x '.join(str(v).replace('.', ',') for v in probable)} cm)" if probable else ""
        issue(p, "medida-malformada", f"{label}: \"{raw}\" está com erro de digitação{hint}")
        return {"raw": raw, "cm": None, "probable": probable, "unit": unit}
    if unit is None:
        issue(p, "medida-sem-unidade", f"{label}: \"{raw}\" sem unidade (provavelmente cm)")
    return {"raw": raw, "cm": vals, "unit": unit}


def kg(value):
    m = re.search(r"(\d[\d.,]*)\s*kg", value, re.I)
    return num(m.group(1)) if m else None


def liters(value):
    m = re.search(r"(\d[\d.,]*)\s*(l\b|litros?)", value, re.I)
    return num(m.group(1)) if m else None


COLOR_FIX = {
    "branca": "branco", "preta": "preto", "amarela": "amarelo", "vermelha": "vermelho",
    "crú": "cru", "natural": "natural",
}


def parse_colors(value):
    v = re.sub(r"\.$", "", value.strip())
    v = re.sub(r"\s+e\s+", ", ", v)
    out = []
    for c in re.split(r"\s*[,/]\s*", v):
        c = c.strip().lower()
        if not c:
            continue
        c = COLOR_FIX.get(c, c)
        if c not in out:
            out.append(c)
    return out


LINE_RE = re.compile(r"^(?P<label>[^–\-:]{2,45}?)\s*[–\-:]\s*(?P<value>.+)$")


def lines_of(p):
    t = re.sub(r"<br\s*/?>", "\n", p["short_description"])
    t = re.sub(r"</p>\s*<p>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t))
    t = t.replace(" ", " ")
    return [re.sub(r"\s+", " ", l).strip() for l in t.split("\n") if l.strip()]


def build(p):
    ls = lines_of(p)
    rec = {
        "id": p["id"],
        "name": DISPLAY_NAME.get(p["slug"], clean_name(p["name"])),
        "oldName": re.sub(r"\s+", " ", html.unescape(p["name"])).strip(),
        "slug": NEW_SLUG.get(p["slug"]) or slugify(DISPLAY_NAME.get(p["slug"], clean_name(p["name"]))),
        "oldSlug": p["slug"],
        "oldUrl": p["permalink"],
        "category": None,
        "subcategory": None,
        "sourceTitle": ls[0] if ls else None,
        "specs": [],              # todas as linhas rotuladas, texto original
        "features": [],           # linhas sem rótulo (fatos do produto)
        "dimensions": {},         # internas / externas / gerais / outras
        "volumeL": None,
        "weightKg": None,
        "m3PerUnit": None,
        "colors": [],
        "loads": [],              # {label, kg, raw}
        "packaging": None,
        "lidOptional": False,
        "images": [],
        "categoryProvisional": False,
    }

    # categoria
    cats = [c["slug"] for c in p["categories"]]
    mapped = [OLD_CAT[c] for c in cats if c in OLD_CAT]
    if not mapped and p["slug"] in UNCATEGORIZED_GUESS:
        mapped = [UNCATEGORIZED_GUESS[p["slug"]]]
        rec["categoryProvisional"] = True
        issue(p, "categoria", "sem categoria no site antigo; categoria provisória atribuída")
    if not mapped and re.search(r"lixeira", p["name"], re.I):
        mapped = [("lixeiras", "lixeiras-basculantes" if "basculante" in p["name"].lower() else "lixeiras-plasticas")]
        rec["categoryProvisional"] = True
        issue(p, "categoria", "sem categoria no site antigo; categoria provisória atribuída")
    if mapped:
        subs = [m for m in mapped if m[1]]
        subs.sort(key=lambda m: (0 if m[1] in SUB_PRIORITY else 1))
        rec["category"] = (subs[0] if subs else mapped[0])[0]
        rec["subcategory"] = subs[0][1] if subs else None
        if len({m[0] for m in mapped}) > 1:
            issue(p, "categoria", f"aparece em mais de uma categoria no site antigo: {cats}")
    else:
        issue(p, "categoria", f"sem categoria reconhecida: {cats}")

    for line in ls[1:]:
        m = LINE_RE.match(line)
        if not m:
            if re.fullmatch(r"tampa opcional", line, re.I):
                rec["lidOptional"] = True
            if line.rstrip(":–- ").lower() == "acompanha":
                rec["features"].append(line)
                continue
            rec["features"].append(line)
            continue
        label, value = m.group("label").strip(), m.group("value").strip()
        low = label.lower()
        rec["specs"].append({"label": label, "value": value})

        if low.startswith("medidas interna"):
            rec["dimensions"]["internal"] = parse_dims(p, label, value)
        elif low.startswith("medidas externa"):
            rec["dimensions"]["external"] = parse_dims(p, label, value)
        elif low == "medidas":
            rec["dimensions"]["overall"] = parse_dims(p, label, value)
        elif low.startswith("medidas") or low.startswith("comprimento"):
            rec["dimensions"].setdefault("other", []).append({"label": label, **parse_dims(p, label, value)})
        elif low in ("cores disponíveis", "disponíveis nas cores", "cor disponível") or low.startswith("cores disp"):
            rec["colors"] = parse_colors(value)
        elif low == "peso" or low.startswith("peso "):
            v = kg(value)
            if low == "peso":
                rec["weightKg"] = v
            if v is None:
                issue(p, "peso", f"{label}: \"{value}\" não pôde ser lido")
            elif low != "peso":
                rec["loads"].append({"label": label, "kg": v, "raw": value, "kind": "peso"})
            if re.search(r"\d\.\d{3}\s*kg", value, re.I) and v and v > 1000:
                issue(p, "peso", f"{label}: \"{value}\" — ponto pode ser milhar ou decimal (provável {v/1000:g} kg); confirmar")
                if low == "peso":
                    rec["weightKg"] = None
                rec["loads"] = [l for l in rec["loads"] if l["raw"] != value]
        elif low == "cubagem":
            mm = re.search(r"(\d[\d.,]*)\s*m", value)
            rec["m3PerUnit"] = num(mm.group(1)) if mm else None
        elif low == "capacidade":
            l = liters(value)
            if l is not None:
                rec["volumeL"] = l
                if re.search(r"/|cada", value):
                    rec["specs"][-1]["note"] = "capacidade composta"
            else:
                k = kg(value)
                if k is not None:
                    rec["loads"].append({"label": "Capacidade", "kg": k, "raw": value})
                else:
                    issue(p, "capacidade", f"\"{value}\" não pôde ser lida")
        elif low == "embalagem":
            rec["packaging"] = value
        elif "carga" in low or "capacidade" in low or low in ("no rack", "porta pallet"):
            rec["loads"].append({"label": label, "kg": kg(value), "raw": value})
        # outras linhas (diâmetro das rodas, prolongador, acompanha...) ficam só em specs

    # imagens
    seen = set()
    for i, img in enumerate(p["images"]):
        src = img["src"]
        if src in seen:
            continue
        seen.add(src)
        rec["images"].append({"src": src, "original": re.sub(r"-scaled(\.\w+)$", r"\1", src), "oldAlt": img.get("alt", "")})

    # --- validações -----------------------------------------------------
    d = rec["dimensions"]
    ext = (d.get("external") or d.get("overall") or {}).get("cm")
    if rec["m3PerUnit"] is not None:
        if ext and len(ext) == 3:
            calc = ext[0] * ext[1] * ext[2] / 1_000_000
            ratio = rec["m3PerUnit"] / calc if calc else 0
            if not (0.85 <= ratio <= 1.15):
                issue(p, "cubagem", f"cubagem informada {rec['m3PerUnit']} m³ ≠ medidas externas {ext} ({calc:.4f} m³)")
        elif not (d.get("external") or {}).get("probable"):
            issue(p, "cubagem", "cubagem informada mas sem medidas externas completas para conferir")
    if d.get("internal", {}).get("cm") and rec["volumeL"]:
        i_ = d["internal"]["cm"]
        if len(i_) == 3:
            calc_l = i_[0] * i_[1] * i_[2] / 1000
            if not (0.6 <= rec["volumeL"] / calc_l <= 1.15):
                issue(p, "volume", f"volume {rec['volumeL']} L vs medidas internas {i_} (~{calc_l:.1f} L)")
    if d.get("internal", {}).get("cm") and ext and len(d["internal"]["cm"]) == len(ext):
        if any(a > b for a, b in zip(d["internal"]["cm"], ext)):
            issue(p, "medidas", f"medida interna {d['internal']['cm']} maior que externa {ext}")
    probable_ext = (d.get("external") or {}).get("probable")
    if rec["m3PerUnit"] is not None and probable_ext and len(probable_ext) == 3:
        calc = probable_ext[0] * probable_ext[1] * probable_ext[2] / 1_000_000
        if not (0.85 <= rec["m3PerUnit"] / calc <= 1.15):
            issue(p, "cubagem", f"cubagem informada {rec['m3PerUnit']} m³ ≠ medidas externas prováveis {probable_ext} ({calc:.4f} m³)")
        else:
            issues.pop() if issues and issues[-1]["kind"] == "cubagem" and issues[-1]["slug"] == p["slug"] else None
    if p["slug"] in DISPLAY_NAME:
        issue(p, "nome", f"nome repetido no site antigo (\"{rec['oldName']}\"); exibido como \"{rec['name']}\"")
    if not d:
        issue(p, "dados-faltando", "sem medidas")
    if rec["weightKg"] is None and not any(l.get("kind") == "peso" for l in rec["loads"]):
        issue(p, "dados-faltando", "sem peso")
    if not rec["colors"]:
        issue(p, "dados-faltando", "sem cores")
    if not rec["images"]:
        issue(p, "sem-foto", "produto sem foto")
    return rec


def main():
    raw = []
    for f in RAW:
        raw += json.load(open(f))
    products = [build(p) for p in raw]

    # nomes de arquivo de imagem por produto
    manifest = []
    slugs = {pr["slug"] for pr in products}
    for pr in products:
        for n, img in enumerate(pr["images"], 1):
            ext = img["original"].rsplit(".", 1)[1].lower().replace("jpeg", "jpg")
            base = pr["slug"] if n == 1 else f"{pr['slug']}-{n}"
            if n > 1 and base in slugs:  # colide com o slug de outro produto
                base = f"{pr['slug']}-foto-{n}"
            img["file"] = f"{base}.{ext}"
            img["base"] = base
            manifest.append({"url": img["original"], "fallback": img["src"], "file": img["file"]})

    # slugs duplicados?
    from collections import Counter
    for s, c in Counter(p["slug"] for p in products).items():
        if c > 1:
            issues.append({"slug": s, "name": s, "kind": "slug", "detail": f"slug repetido {c}x"})
    # nomes parecidos (possíveis duplicados)
    names = Counter(slugify(p["name"]) for p in products)
    for n, c in names.items():
        if c > 1:
            issues.append({"slug": n, "name": n, "kind": "duplicado", "detail": f"{c} produtos com o mesmo nome"})

    # redirecionamentos 301 (URLs antigas -> novas) e 410 (lixo do tema WP)
    redirects = []
    for pr in products:
        if pr["category"]:
            redirects.append({"from": f"/produto/{pr['oldSlug']}/", "to": f"/produtos/{pr['category']}/{pr['slug']}/"})
    parent_of = {}
    for c in json.load(open(ROOT / "raw/categories.json")):
        parent_of[c["slug"]] = c["parent"]
    id_to_slug = {c["id"]: c["slug"] for c in json.load(open(ROOT / "raw/categories.json"))}
    for old, (new, sub) in OLD_CAT.items():
        target = f"/produtos/{new}/" + (f"{sub}/" if sub else "")
        redirects.append({"from": f"/product-category/{old}/", "to": target})
        if parent_of.get(old):  # WP usa /product-category/pai/filho/
            redirects.append({"from": f"/product-category/{id_to_slug[parent_of[old]]}/{old}/", "to": target})
    redirects += [
        {"from": "/product-category/uncategorized/", "to": "/produtos/"},
        {"from": "/sobre-nos/", "to": "/sobre/"},
        {"from": "/fale-conosco/", "to": "/contato/"},
        {"from": "/faq/", "to": "/contato/"},
        {"from": "/shop/", "to": "/produtos/"},
        {"from": "/loja/", "to": "/produtos/"},
    ]
    keep = {"/", "/produtos/"} | {r["from"] for r in redirects}
    gone = []
    sm = ROOT / "raw/old-sitemap/urls.txt"
    if sm.exists():
        for u in sm.read_text().split():
            pth = re.sub(r"^https?://[^/]+", "", u)
            if pth not in keep:
                gone.append(pth)
    json.dump({"redirects": redirects, "gone": sorted(set(gone))}, open(OUT / "redirects.json", "w"), ensure_ascii=False, indent=1)

    cats_out = [
        {"slug": s, "name": n, "subcategories": [{"slug": ss, "name": nn,
            "count": sum(1 for p in products if p["subcategory"] == ss)} for ss, nn in subs],
         "count": sum(1 for p in products if p["category"] == s)}
        for s, n, subs in CATEGORIES
    ]

    json.dump(products, open(OUT / "products.json", "w"), ensure_ascii=False, indent=1)
    json.dump(cats_out, open(OUT / "categories.json", "w"), ensure_ascii=False, indent=1)
    json.dump(manifest, open(OUT / "images-manifest.json", "w"), ensure_ascii=False, indent=1)
    json.dump(issues, open(OUT / "issues.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(products)} produtos, {len(manifest)} imagens, {len(redirects)} redirecionamentos, {len(issues)} pendências")
    for c in cats_out:
        print(f"  {c['slug']}: {c['count']}", {s['slug']: s['count'] for s in c['subcategories']})


if __name__ == "__main__":
    main()
