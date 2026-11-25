#!/usr/bin/env bash
# Baixa as fotos originais listadas em data/images-manifest.json e data/pj-images-manifest.json.
set -uo pipefail
cd "$(dirname "$0")/.."
mkdir -p assets/originals/pj/sem-associacao assets/originals/pj/conteudo
python3 -c "
import json
for m in json.load(open('data/images-manifest.json')): print(m['url'],m['fallback'],m['file'],sep='\t')
for m in json.load(open('data/pj-images-manifest.json')): print(m['url'],m['url'],m['file'],sep='\t')
" | xargs -P 6 -d '\n' -I{} bash -c 'IFS=$'"'"'\t'"'"' read -r a b c <<< "{}"; ./scripts/fetch-images.sh "$a" "$b" "$c"'
