// Fase (a), passo 4: gera WebP e AVIF em 480/768/1200 px a partir de
// assets/originals/ (os originais nunca são alterados).
// Saída: public/img/<mesmo caminho relativo>-<largura>.<webp|avif>
//        data/image-variants.json  { "<caminho sem extensão>": {w, h, widths[]} }
// Não amplia imagens: se o original for menor que 480 px, gera só no tamanho original.
import { readdir, mkdir, stat, writeFile, readFile } from "node:fs/promises";
import path from "node:path";
import sharp from "sharp";

const ROOT = path.resolve(import.meta.dirname, "..");
const SRC = path.join(ROOT, "assets/originals");
const OUT = path.join(ROOT, "public/img");
const WIDTHS = [480, 768, 1200];
const EXTS = new Set([".jpg", ".jpeg", ".png", ".webp", ".gif"]);
const CONCURRENCY = 4;

async function walk(dir) {
  const out = [];
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) out.push(...(await walk(p)));
    else if (EXTS.has(path.extname(e.name).toLowerCase())) out.push(p);
  }
  return out;
}

async function exists(p) {
  try { await stat(p); return true; } catch { return false; }
}

async function processOne(file, variants) {
  const rel = path.relative(SRC, file);
  const key = rel.slice(0, -path.extname(rel).length).split(path.sep).join("/");
  const img = sharp(file, { animated: false }).rotate();
  const meta = await img.metadata();
  // dimensões já com a rotação EXIF aplicada
  const swap = meta.orientation && meta.orientation >= 5;
  const w0 = swap ? meta.height : meta.width;
  const h0 = swap ? meta.width : meta.height;
  let widths = WIDTHS.filter((w) => w <= w0);
  if (widths.length === 0) widths = [w0];
  await mkdir(path.dirname(path.join(OUT, rel)), { recursive: true });
  for (const w of widths) {
    const base = path.join(OUT, `${key}-${w}`);
    if (!(await exists(`${base}.webp`))) {
      await sharp(file).rotate().resize({ width: w, withoutEnlargement: true })
        .webp({ quality: 78, effort: 5 }).toFile(`${base}.webp`);
    }
    if (!(await exists(`${base}.avif`))) {
      await sharp(file).rotate().resize({ width: w, withoutEnlargement: true })
        .avif({ quality: 55, effort: 4 }).toFile(`${base}.avif`);
    }
  }
  variants[key] = { w: w0, h: h0, widths, hasAlpha: !!meta.hasAlpha, format: meta.format };
}

const files = await walk(SRC);
const variants = {};
let done = 0;
const queue = [...files];
await Promise.all(
  Array.from({ length: CONCURRENCY }, async () => {
    while (queue.length) {
      const f = queue.shift();
      try {
        await processOne(f, variants);
      } catch (e) {
        console.error("ERRO", path.relative(ROOT, f), e.message);
      }
      if (++done % 50 === 0) console.log(`${done}/${files.length}`);
    }
  }),
);
const sorted = Object.fromEntries(Object.entries(variants).sort());
await writeFile(path.join(ROOT, "data/image-variants.json"), JSON.stringify(sorted, null, 1));
console.log(`ok: ${Object.keys(sorted).length} imagens`);
