#!/usr/bin/env bash
# Fase (a): baixa os dados brutos do site antigo e da PJ para raw/.
# Depois rode: npm run data && bash scripts/download-originals.sh && npm run images
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p raw/pj/html raw/old-sitemap
OLD=https://plasdistribuidora.com.br
for p in 1 2 3; do
  curl -fsS --max-time 60 "$OLD/wp-json/wc/store/v1/products?per_page=100&page=$p" -o "raw/products-$p.json" || true
  [ "$(python3 -c "import json;print(len(json.load(open('raw/products-$p.json'))))" 2>/dev/null || echo 0)" = 0 ] && rm -f "raw/products-$p.json" && break
done
curl -fsS --max-time 60 "$OLD/wp-json/wc/store/v1/products/categories?per_page=100" -o raw/categories.json
curl -fsSL --max-time 30 "$OLD/wp-sitemap.xml" | grep -o '<loc>[^<]*' | sed 's/<loc>//' \
  | while read -r u; do curl -fsSL --max-time 30 "$u"; done | grep -o '<loc>[^<]*' | sed 's/<loc>//' > raw/old-sitemap/urls.txt
curl -fsS --max-time 30 https://pjcomercial.com.br/sitemap.xml | grep -o '<loc>[^<]*' | sed 's/<loc>//' > raw/pj/urls.txt
while read -r u; do
  n=$(basename "$u"); [ "$u" = "https://pjcomercial.com.br" ] && n=home
  curl -fsS --max-time 30 "$u" -o "raw/pj/html/$n.html" || echo "falhou $u"
done < raw/pj/urls.txt
echo "ok"
