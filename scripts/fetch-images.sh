#!/usr/bin/env bash
# Baixa uma imagem original (sem -scaled); se não existir, usa a versão "scaled".
# Uso: fetch-images.sh URL FALLBACK ARQUIVO
set -u
out="assets/originals/$3"
[ -s "$out" ] && exit 0
curl -fsS --retry 3 --max-time 120 "$1" -o "$out" 2>/dev/null || curl -fsS --retry 3 --max-time 120 "$2" -o "$out" || echo "FALHOU $3 $1"
