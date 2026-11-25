#!/usr/bin/env python3
"""Gera PENDENCIAS.md a partir de data/issues.json, data/products.json,
data/pj-products.json e data/image-variants.json."""
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D = ROOT / "data"
products = json.load(open(D / "products.json"))
issues = json.load(open(D / "issues.json"))
pj = json.load(open(D / "pj-products.json"))
variants = json.load(open(D / "image-variants.json")) if (D / "image-variants.json").exists() else {}
cats = {c["slug"]: c["name"] for c in json.load(open(D / "categories.json"))}
by_old = {p["oldSlug"]: p for p in products}

def br(t):
    """[16.5, 59.8, 70.6] -> 16,5 x 59,8 x 70,6 cm; 0.088 -> 0,088"""
    t = re.sub(r"\[([\d., ]+)\]", lambda m: " x ".join(x.strip() for x in m.group(1).split(",")) + " cm", t)
    t = re.sub(r"(\d+)\.(\d+)(?!\d* ?Kg\.\")", r"\1,\2", t)
    return t.replace("≠", "não bate com")


THIRD_PARTY = ["larplasticos", "arcos", "galia", "maxicaixa", "ecopallet", "smart"]

L = []
w = L.append
w("# Pendências")
w("")
w("**Status: fase (a), extração de dados e imagens, concluída em 25/11/2026.** Fase (b): proposta visual em `design/proposta-visual.md`, aguardando aprovação do dono.")
w("")
w("Gerado por `scripts/pendencias.py` a partir dos dados do site antigo. **Nada aqui foi corrigido por conta própria.**")
w("")
w("Decisões do dono (25/11/2026), registradas também em `DECISOES.md`:")
w("")
w("- Os dados das seções 1 a 3 vão para o site **como estão escritos no site antigo**; o dono corrige depois, se for o caso.")
w("- Os produtos que só existem na PJ (seção 8) **entram no site**.")
w("- Produtos sem peso ficam **sem peso** (seção 6).")
w("- O uso de todas as fotos (inclusive as com nome de fabricante) **está liberado**.")
w("")
w(f"Resumo: **{len(products)} produtos**, **{sum(len(p['images']) for p in products)} fotos de produto no catálogo**, "
  f"**{sum(len(o['images']) for o in pj)} fotos de produto da PJ** ({sum(1 for o in pj if o['match'])} produtos da PJ associados).")
w("")

# 1. erros de digitação / inconsistências
def section(title, kinds, note=None):
    rows = [i for i in issues if i["kind"] in kinds]
    if not rows:
        return
    w(f"## {title}")
    w("")
    if note:
        w(note)
        w("")
    w("| Produto | Problema |")
    w("|---|---|")
    for i in rows:
        p = by_old.get(i["slug"])
        name = p["name"] if p else i["name"]
        w(f"| {name} | {br(i['detail'])} |")
    w("")

section("1. Medidas com erro de digitação ou sem unidade", {"medida-malformada", "medida-sem-unidade"})
section("2. Cubagem (m³/unidade) e volume que não batem com as medidas", {"cubagem", "volume"},
        "Conferido em todos os produtos que informam cubagem: m³ = altura x largura x comprimento das medidas externas. "
        "Tolerância de 15%.")
section("3. Pesos com número ambíguo", {"peso"})
section("4. Categoria", {"categoria"},
        "Produtos sem categoria no site antigo receberam uma categoria provisória pelo nome. Confirmar.")
section("5. Produtos com o mesmo nome no site antigo", {"nome"},
        "Para o cliente conseguir diferenciar, o nome exibido ganhou a capacidade ou a medida (tirada dos próprios dados). Confirmar se o dono prefere outro nome (ex.: código do fabricante).")

# 6. dados faltando
miss = defaultdict(list)
for i in issues:
    if i["kind"] == "dados-faltando":
        p = by_old.get(i["slug"])
        miss[p["name"] if p else i["name"]].append(i["detail"].replace("sem ", ""))
if miss:
    w("## 6. Dados faltando")
    w("")
    w("Decisão do dono: esses produtos ficam sem o campo na ficha técnica. Lista mantida só para referência.")
    w("")
    w("| Produto | Falta |")
    w("|---|---|")
    for n, f in sorted(miss.items()):
        w(f"| {n} | {', '.join(f)} |")
    w("")

# 7. fotos
noimg = [p["name"] for p in products if not p["images"]]
low = []
for p in products:
    if not p["images"]:
        continue
    key = p["images"][0]["file"].rsplit(".", 1)[0]
    v = variants.get(key)
    if v and v["w"] < 768:
        low.append((p["name"], v["w"], v["h"]))
w("## 7. Fotos")
w("")
w(f"- Produtos sem foto: {', '.join(noimg) if noimg else 'nenhum'}.")
w(f"- Foto principal com menos de 768 px de largura ({len(low)} produtos). Funciona, mas fica pequena em tela grande; vale pedir fotos melhores:")
w("")
for n, ww, hh in sorted(low, key=lambda x: x[1]):
    w(f"  - {n} ({ww} x {hh} px)")
w("")
w("- Fotos com nome de fabricante no arquivo: uso liberado pelo dono (resolvido).")
w("")

# 8. PJ
w("## 8. PJ Comercial")
w("")
pj_only = [p for p in products if p.get("source") == "pj"]
w("Produtos que existem só na PJ. **Decisão do dono: entram no site**, com os dados da página da PJ:")
w("")
for p in pj_only:
    w(f"- **{p['name']}** → `/produtos/{p['category']}/{p['slug']}/`")
w("")
unmatched = [o for o in pj if not o["match"]]
if unmatched:
    w("Fotos da PJ que não foram associadas a nenhum produto (ficam em `assets/originals/pj/sem-associacao/`):")
    w("")
    for o in unmatched:
        w(f"- **{o['pjTitle']}**: {o['pjDesc'][:160].strip()} (não dá para saber se é a Miami ou a Miami Club)")
    w("")
w("Observação: o briefing diz que a PJ não tem medidas, mas várias páginas da PJ têm. Os dados técnicos do site novo vêm só da PLAS.")
w("")

# 9. mudanças de nome/endereço
changed = [p for p in products if p["oldSlug"] and p["slug"] != p["oldSlug"]]
w("## 9. Endereços (URLs) que mudaram")
w("")
w(f"{len(changed)} produtos tinham endereço antigo diferente do nome (ex.: o \"Kit Completo do Carrinho Funcional de Limpeza\" "
  "estava em `/produto/placa-sinalizadora-sem-mensagem/`). Todos ganham endereço novo pelo nome, com redirecionamento 301 "
  "do antigo (`data/redirects.json`). Só para conhecimento.")
w("")
for p in changed:
    w(f"- `/produto/{p['oldSlug']}/` → `/produtos/{p['category']}/{p['slug']}/`")
w("")

w("## 10. Pendências gerais com o dono (do briefing)")
w("")
for done, item in [
    (False, "**WhatsApp da PLAS** (com DDD), para o botão de orçamento"),
    (False, "**Plano da Hostinger**: roda PHP? `.htaccess` funciona? (decide o formulário de orçamento)"),
    (False, "**CNPJ e endereço completo**, para o rodapé, o Google Meu Negócio e os dados estruturados"),
    (False, "**Logo em alta resolução**, de preferência SVG. O atual é PNG 500 x 500 px, todo em cinza-grafite (#484343), sem cor"),
    (False, "URL do **Profitize** (templates), se quiser que seja usado como fonte"),
    (True, "Skills da Emil: instaladas"),
    (False, "Autorização para usar Google Analytics (se desejado)"),
    (True, "Referências visuais: o dono não tem; aprovou a recomendação, com azul de destaque"),
    (False, "**Escolher a variação do hero** (Catálogo, Ficha técnica ou Setores) e aprovar a proposta visual"),
    (True, "Medidas a confirmar: publicar como estão (decisão do dono)"),
    (True, "Lista completa de produtos: a API trouxe os 159 do sitemap antigo + 2 só da PJ = 161"),
    (True, "Uso das fotos: liberado"),
]:
    w(f"- [{'x' if done else ' '}] {item}")
w("")

(ROOT / "PENDENCIAS.md").write_text("\n".join(L), encoding="utf-8")
print(f"PENDENCIAS.md: {len(L)} linhas")
