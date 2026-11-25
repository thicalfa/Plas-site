#!/usr/bin/env python3
"""Gera data.js do protótipo da home a partir de data/products.json."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
ps = json.load(open(ROOT / "data/products.json"))
cats = {c["slug"]: c["name"] for c in json.load(open(ROOT / "data/categories.json"))}
variants = json.load(open(ROOT / "data/image-variants.json"))


def litros(p):
    if p["volumeL"]:
        return p["volumeL"]
    m = re.search(r"(\d+(?:,\d+)?)\s*litros", p["name"], re.I)  # capacidade escrita no nome
    return float(m.group(1).replace(",", ".")) if m else None


def img(p):
    k = p["images"][0]["file"].rsplit(".", 1)[0]
    return f"../../../public/img/{k}-{variants[k]['widths'][0]}.webp"


out = []
for p in ps:
    out.append({"s": p["slug"], "n": p["name"], "c": p["category"], "cn": cats[p["category"]],
                "l": litros(p), "i": img(p)})
SETORES = [
    ("hospitais", "Hospitais e clínicas", "Lixeiras com pedal para não tocar na tampa, containers para resíduo e carros de limpeza.",
     ["lixeira-quadrada-60-litros-com-pedal", "container-plastico-660-litros-com-pedal", "kit-completo-do-carrinho-funcional-de-limpeza", "lixeira-plastica-para-descarte-de-pilhas-e-baterias-40-litros"]),
    ("hoteis", "Hotéis e pousadas", "Móveis para área da piscina e do jardim, lixeiras para áreas comuns e caixas para o estoque.",
     ["espreguicadeira-miami-club", "mesa-plastica-redonda", "poltrona-com-braco", "lixeira-papeleira-50-litros"]),
    ("supermercados", "Supermercados e padarias", "Cestos de compra, cestos de pão, caixas térmicas para frios e coleta seletiva.",
     ["cesto-supermercado", "cesto-de-pao-40-litros", "caixa-frigorifica-42-litros", "conjunto-coleta-seletiva-4-lixeiras-60-litros"]),
    ("hortifrutis", "Hortifrutis e Ceasa", "Caixas vazadas que deixam o ar circular, bandejas e estrados para tirar a mercadoria do chão.",
     ["caixa-hortifruti-vazada-46-litros", "caixa-vazada-60-litros", "bandeja-18", "estrado-50x50-cm"]),
    ("industrias", "Indústrias", "Caixas KLT padronizadas, gaveteiros para peças e pallets de contenção para tambores.",
     ["caixa-rl-klt-4322", "gaveteiro-05", "pallet-contencao-4-tambores-420-litros", "caixa-fechada-61-litros"]),
    ("logistica", "Logística e armazéns", "Pallets plásticos, caixas pallet dobráveis e carros para mover caixas entre setores.",
     ["pallet-plastico-vazado", "caixa-pallet-glt", "pallet-plastico-klt", "carro-para-caixa-180-litros"]),
]
slugs = {p["s"] for p in out}
for _, _, _, items in SETORES:
    for s in items:
        assert s in slugs, s
data = {"produtos": out, "setores": [{"id": a, "nome": b, "texto": c, "itens": d} for a, b, c, d in SETORES]}
(Path(__file__).parent / "data.js").write_text("window.PLAS = " + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";\n")
print(len(out), "produtos;", sum(1 for p in out if p["l"]), "com litros")
