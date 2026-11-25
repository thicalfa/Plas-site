# BRIEFING: Site da PLAS Distribuidora

> Cole este arquivo na raiz de uma pasta nova e vazia no seu computador (ex.: `plas-site`) e abra o Claude Code nessa pasta. Se preferir, renomeie para `CLAUDE.md` para ele ler sozinho toda vez.

## 1. Objetivo
Criar o novo site da **PLAS Distribuidora** (B2B, produtos plásticos). O site deve ser bonito, moderno, rápido, seguro, sem erros e bem posicionado no Google. A conversão principal é **pedido de orçamento** (formulário + WhatsApp). Não há preço nem carrinho.

## 2. Contexto
- Empresa: PLAS Distribuidora, Santo André/SP. Vende para hospitais, hotéis, mercados, hortifrutis, indústrias, logística e outros.
- Site antigo (WordPress/WooCommerce): https://plasdistribuidora.com.br/ (fonte dos produtos, textos e fotos).
- Empresa irmã (mesmo dono, mesmos produtos, outro CNPJ): https://pjcomercial.com.br/ (feita no Hostinger AI Builder). Ela tem poucas fotos e **nenhuma medida**. Serve só como fonte extra de imagens.
- Domínio: `plasdistribuidora.com.br` (já do dono). Hospedagem: Hostinger.
- Contato (do site antigo): tel. (11) 4421-1714, vendas@plasdistribuidora.com.br, Instagram e Facebook `plasdistribuidora`.

## 3. Regras de conteúdo
- Português do Brasil, tom profissional e direto.
- **Todo texto deve ser original.** Não copiar textos da PJ nem do site antigo palavra por palavra (conteúdo repetido entre os dois sites prejudica o Google). As fotos e os dados técnicos podem ser reaproveitados, pois são do dono.
- Cada produto precisa de: nome, categoria, descrição própria, ficha técnica (medidas, volume, peso, cores), aplicações, foto com texto alternativo único.
- Nunca inventar medidas ou dados. Se faltar dado, listar em `PENDENCIAS.md`.

## 4. Tarefa 1: extrair produtos e imagens (fazer primeiro)
1. Em `https://plasdistribuidora.com.br/` tente a API da loja: `/wp-json/wc/store/v1/products?per_page=100&page=N` (percorra todas as páginas). Se não funcionar, use `/wp-json/wp/v2/media`, o `sitemap.xml` ou leia as páginas de categoria e produto (o site tem botão "Load More", então há mais produtos do que a home mostra).
2. Para cada produto salve em `data/products.json`: nome, slug, categoria e subcategoria, descrição, medidas internas/externas, volume (L), peso (kg), m³/unidade, cores, capacidade de carga (se houver), URLs das imagens.
3. Baixe as imagens em **tamanho original** (não as miniaturas tipo `-150x150`) para `assets/originals/`. Nomeie por produto: `caixa-fechada-06.jpg`, `caixa-fechada-06-2.jpg`, etc.
4. Gere versões otimizadas em WebP (e AVIF se possível) em `public/img/`, em larguras 480/768/1200. Nunca altere os originais.
5. Da PJ (`pjcomercial.com.br`), baixe também as imagens de conteúdo. As URLs ficam no HTML (`assets.zyrosite.com`). Tente o arquivo original removendo o trecho `cdn-cgi/image/...`. Salve em `assets/originals/pj/`.
6. Gere `PENDENCIAS.md` com: produtos sem foto, dados faltando e inconsistências.

### Inconsistências já conhecidas (confirmar com o dono, não corrigir sozinho)
- **Cesto de Pão (versão 1)**: medida externa vem como "15,5,0 x 58,0 x 66,5 cm" (provável 15,5).
- **Cesto de Pão (versão 2)**: medida externa vem como "16,5,0 x 59,8 x 70,6 cm" (provável 16,5).
- **Bandeja 04**: 0,088 m³/unidade é incompatível com as medidas externas (7 x 30 x 42 cm dá cerca de 0,0088 m³).
- **Espreguiçadeiras**: dimensões sem unidade (28 x 67 x 190, provavelmente cm).
- Em geral: validar se m³/unidade bate com as medidas externas em todos os produtos.

### Produtos já vistos no site antigo (20 de uma lista que tem mais)
Categorias: Caixas Plásticas (Vazadas, KLT, Fechadas), Bandejas, Lixeiras (Coleta Seletiva, Basculante, Pedal, Plásticas), Pallets (Contenção, Plástico, Rotomoldados), Containers e Carros, Estrados, Cestos e Gaveteiros, Móveis Plásticos (Cadeiras, Mesas, Espreguiçadeiras, Banquetas).

| Produto | Categoria | Medidas internas (cm) | Medidas externas (cm) | Volume | Peso | Cores |
|---|---|---|---|---|---|---|
| Caixa Fechada 03 | Caixas Fechadas | 10,0 x 22,5 x 30,0 | 12,3 x 27,0 x 39,0 | 6,5 L | 0,450 kg | preto, azul |
| Caixa Fechada 05 | Caixas Fechadas | 18,0 x 29,0 x 37,5 | 20,0 x 33,0 x 47,0 | 18 L | 1,000 kg | preto, azul |
| Caixa Fechada 06 | Caixas Fechadas | 15,0 x 22,5 x 51,0 | 18,0 x 24,5 x 57,5 | 12 L | 0,992 kg | natural, azul |
| Caixa Fechada 50 litros | Caixas Plásticas | 22,4 x 36,3 x 56,0 | 24,0 x 40,0 x 60,0 | 45,5 L | 2,426 kg | branco, preto, azul |
| Caixa Fechada 74 litros | Caixas Plásticas | 33,0 x 36,0 x 61,5 | 35,0 x 41,0 x 68,0 | 74 L | 2,200 kg | branco, preto, azul |
| Caixa Fechada 130 litros | Caixas Fechadas | 40,0 x 51,0 x 69,0 | 41,0 x 56,0 x 78,0 | 130 L | 4,966 kg | branco, preto, azul |
| Caixa Vazada 64 | Caixas Vazadas | 5,6 x 36,5 x 48,5 | 6,4 x 40,0 x 60,0 | 10 L | 0,900 kg | branco, verde |
| Caixa Vazada 78 | Caixas Vazadas | 6,8 x 36,5 x 56,0 | 7,8 x 40,0 x 60,0 | 12 L | 1,000 kg | verde, natural |
| Bandeja 02 | Bandejas | 5,0 x 16,5 x 27,0 | 5,5 x 19,5 x 30,0 | 2,2 L | 0,156 kg | branco |
| Bandeja 04 | Bandejas | 6,5 x 26,0 x 36,0 | 7,0 x 30,0 x 42,0 | 6 L | 0,434 kg | branco, preto |
| Bandeja 08 | Bandejas | 5,8 x 25,5 x 30,7 | 6,0 x 28,0 x 33,0 | 4,5 L | 0,268 kg | branco |
| Bandeja 09 | Bandejas | 6,3 x 26,0 x 43,0 | 6,5 x 29,0 x 46,0 | 7 L | 0,360 kg | branco |
| Bandeja 18 | Bandejas | 8,5 x 34,0 x 53,0 | 9,0 x 40,0 x 60,0 | 18 L | 1,000 kg | branco |
| Cesto de Pão (v1) | Cestos | 12,0 x 54,0 x 62,5 | 15,5 x 58,0 x 66,5 (confirmar) | 40 L | 2,066 kg | branco, preto, laranja, verde, azul, amarelo, vermelho |
| Cesto de Pão (v2) | Cestos | 14,5 x 56,8 x 66,0 | 16,5 x 59,8 x 70,6 (confirmar) | 51 L | 2,076 kg | natural, preto, laranja, verde, azul, vermelho |
| Cesto Supermercado | Cestos | 16,3 x 27,0 x 41,0 | 20,0 x 29,5 x 44,5 | 13 L | 0,640 kg | branco, preto, laranja, verde, azul, amarelo |
| Estrado 1060 | Estrados | n/d | 4,5 x 60,0 x 100,0 | n/d | 4,370 kg | branco, preto, azul, natural, cinza, verde |
| Poltrona com braço | Móveis Plásticos | n/d | 90 x 56 x 58 | n/d | carga 182 kg | branco, preto |
| Espreguiçadeira Miami | Móveis Plásticos | n/d | 28 x 67 x 190 | n/d | 10 kg, carga 140 kg | branco |
| Espreguiçadeira Miami Club | Móveis Plásticos | n/d | 28 x 67 x 190 | n/d | 10 kg, carga 140 kg | branco |

> A tabela acima é só ponto de partida. A fonte da verdade é o que a Tarefa 1 extrair.

## 5. Stack e hospedagem
- **Astro + Tailwind CSS**, site estático (HTML pronto, sem servidor). Produtos vêm de `data/products.json`, e as páginas são geradas automaticamente.
- Publicação na Hostinger: gerar `dist/` e enviar para `public_html` (FTP/Git). Antes, confirmar o plano da Hostinger e se o `.htaccess` está ativo.
- Formulário de orçamento: como o site é estático, usar um endpoint PHP simples na Hostinger **ou** serviço de formulário. Campos: nome, empresa, setor, telefone, e-mail, produto(s) de interesse, quantidade, mensagem. Validação no cliente e no servidor, campo oculto anti-spam (honeypot), limite de envios, envio para vendas@plasdistribuidora.com.br.
- Botão de WhatsApp com mensagem pré-preenchida (número a confirmar).

## 6. Estrutura de páginas
- `/` Home: proposta de valor, categorias, setores atendidos, produtos em destaque, prova de confiança (entrega, garantia), chamada para orçamento.
- `/produtos/` e `/produtos/[categoria]/`: filtros por categoria, cor e uso.
- `/produtos/[categoria]/[produto]/`: foto, ficha técnica, aplicações, produtos relacionados, botão "Pedir orçamento deste produto".
- `/setores/[setor]/`: hospitais, hotéis, supermercados, hortifrutis, indústrias, logística. Cada página com textos próprios e produtos indicados.
- `/sobre/`, `/contato/` (com orçamento), `/politica-de-privacidade/`, `404`.

## 7. SEO (meta: topo do Google)
- Um `<title>` (até ~60 caracteres) e uma meta description (até ~155) únicos por página. H1 único. URLs limpas e em português.
- Dados estruturados (JSON-LD): `Organization`/`LocalBusiness` (Santo André/SP), `Product` (sem preço, com `brand`, medidas e imagem), `BreadcrumbList`.
- `sitemap.xml`, `robots.txt`, canonical em todas as páginas, Open Graph e Twitter Card com imagem para todas as páginas.
- Texto alternativo descritivo e único em todas as imagens. Nome de arquivo com palavras-chave.
- Redirecionamentos 301 das URLs antigas (`/produto/...`, `/product-category/...`) para as novas, para não perder posição no Google. Gerar o mapa de redirecionamentos na Tarefa 1.
- Metas de performance: Lighthouse 95+ em Performance, SEO, Acessibilidade e Boas Práticas (mobile). LCP < 2,5 s, CLS < 0,1, INP < 200 ms.
- Preparar para Google Search Console e Google Business Profile (conectar o dono depois).

## 8. Segurança
- HTTPS obrigatório (redirecionamento 301 de http para https) e HSTS.
- Cabeçalhos via `.htaccess`: Content-Security-Policy (sem `unsafe-inline` quando possível), `X-Content-Type-Options: nosniff`, `X-Frame-Options`/`frame-ancestors`, `Referrer-Policy`, `Permissions-Policy`.
- Formulário: sanitizar e validar entradas no servidor, proteção contra spam, sem expor e-mail em código sem necessidade.
- Nenhum segredo, senha ou chave no repositório (usar `.env` fora do Git e `.gitignore`).
- `npm audit` limpo, dependências mínimas, sem scripts de terceiros desnecessários.
- **LGPD**: página de privacidade, aviso de cookies apenas se usar analytics ou marketing, consentimento claro no formulário.
- Desativar listagem de diretórios, bloquear acesso a arquivos sensíveis (`.git`, `.env`).

## 9. Design
- Aparência B2B profissional, limpa e moderna, que transmita confiança e robustez. Cores baseadas no logo da PLAS (extrair do arquivo do logo).
- Mobile first, acessível (contraste AA, foco visível, navegação por teclado), animações sutis que respeitam `prefers-reduced-motion`.
- Fotos padronizadas (mesmo enquadramento e fundo quando possível).

### 9.1 Skills de design: instalar e ordem de precedência
Rode cada comando na pasta do projeto, leia a saída completa (se for longa, redirecione para um arquivo temporário e leia o arquivo) e siga as instruções geradas. Caminhos relativos são resolvidos a partir da pasta de arquivos de apoio que o comando informar.

```
npx skills use "https://github.com/leonxlnx/taste-skill" --skill "design-taste-frontend"
npx skills use "https://github.com/pbakaus/impeccable" --skill "impeccable"
npx skills use "https://github.com/microsoft/playwright-cli" --skill "playwright-cli"
```

**Quarta skill (arquivo `e597fed1-skills-main_2.zip`, repositório `emilkowalski/skills`):** o dono vai colocar o zip na pasta do projeto. Extraia e copie para `.claude/skills/` **só** estas: `emil-design-eng`, `review-animations`, `animation-performance`, `break-ui` e `prototype`. Não copie as de Swift, Expo e mobile (`write-swift`, `animate-expo`, `mobile-native`), porque não servem para este site. Alternativa: `npx skills@latest add emilkowalski/skills`.

Skills demais brigam entre si. Por isso, **ordem de precedência** quando houver conflito:

| Ordem | Skill | Papel neste projeto |
|---|---|---|
| 1 | `frontend-design` | Direção estética geral e identidade visual |
| 2 | `design-taste-frontend` | Evitar cara de template genérico ("cara de IA"): tipografia, espaçamento, hierarquia |
| 3 | `web-design-guidelines` | Checagem de UI e acessibilidade |
| 4 | `impeccable` | Revisão crítica e polimento no fim de cada fase |
| 5 | `emil-design-eng` e demais da Emil | Só micro-interações e movimento (hover, transições, entrada de seções) |
| 6 | `playwright-cli` | Testar em navegador real, tirar screenshots (celular e desktop) e checar erros de console |
| 7 | `break-ui` | Estressar os cards e páginas de produto com nomes longos, itens sem foto, listas vazias |

Regras: (a) use no máximo duas skills de design por etapa; (b) se duas discordarem, vale a ordem da tabela e a decisão fica registrada em `DECISOES.md`; (c) **desempenho, acessibilidade, SEO e segurança vencem a estética**: se um efeito pesar no carregamento ou prejudicar a leitura, corte o efeito.

### 9.1.1 O que é "bonito": quem decide é o dono, com referências dele
O Claude Code não deve escolher sozinho o visual. **Antes de propor qualquer layout**, faça isto, nesta ordem:
1. **Peça ao dono as referências dele**: links de sites que ele gosta, componentes ou templates do 21st.dev e do Profitize, e/ou prompts prontos que ele queira usar. Pergunte também o que ele gosta e não gosta em cada um (cores, ritmo, densidade de informação).
2. **Dê a sua recomendação de como o site deveria ser**, em texto curto, para o dono sair procurando referências parecidas: estilo geral (ex.: industrial limpo, moderno corporativo), paleta sugerida a partir do logo, tipo de tipografia, tipo de foto, nível de animação, exemplos de seções que funcionam em sites B2B de indústria e distribuição. Dê também 5 palavras-chave de busca (em português e em inglês) e 3 tipos de sites de referência que ele deveria procurar.
3. Espere o dono responder com as referências. Só então monte a proposta visual da seção 9.2, explicando o que aproveitou de cada referência.

Se o dono não tiver referências, diga isso e siga com a sua recomendação, sem inventar que ele aprovou.

### 9.2 Proposta visual (antes de programar a fase b)
Apresentar ao dono, e esperar aprovação, uma proposta com: paleta (extraída do logo), tipografia (no máximo 2 famílias, com `font-display: swap` e hospedadas no próprio site), grid e layout da home (hero, categorias, setores, produtos em destaque, prova de confiança, CTA de orçamento, rodapé). Gere 2 ou 3 variações do hero em HTML estático (use a skill `prototype`) para o dono escolher.

### 9.3 Templates e componentes: o que coletar (referência visual, não cópia)
O site é feito em código (Astro). Templates de Framer, Webflow ou WordPress **não são importados**: servem como inspiração de layout. Componentes React + Tailwind do 21st.dev podem ser adaptados.

**Fontes**
- **21st.dev**: biblioteca de componentes React + Tailwind no formato shadcn, com comando de instalação por componente e opção de colar o prompt direto no Claude Code. Funciona com Astro, mas a licença não aparece na página principal: **conferir a licença de cada componente antes de usar**. No Astro, use componentes React só onde precisar de interação (`@astrojs/react` em "ilhas"); o resto, converta para Astro para manter o site leve.
- **Profitize**: não consegui localizar esse site de templates. O dono deve passar a URL. Até lá, ignorar esta fonte.
- Inspiração extra (só olhar, não importar): templates industriais/B2B como o Loadex (Webflow, máquinas e indústria) e o B2bizz (Framer, B2B).

**O que coletar (até 3 candidatos por item; o dono escolhe)**
1. Hero sóbrio, com foto de produto e CTA de orçamento (sem shader, WebGL, 3D ou fundo animado pesado).
2. Navegação com menu de categorias (mega-menu) e botão "Pedir orçamento" fixo.
3. Card e grade de produtos, com filtro por categoria e cor.
4. Galeria da página de produto (zoom leve, miniaturas).
5. Ficha técnica (tabela responsiva de medidas).
6. Faixa de números/diferenciais (entrega, garantia, atendimento).
7. Seção "setores atendidos" (hospitais, hotéis, mercados, hortifrutis, indústrias).
8. Depoimentos e logos de clientes (só com autorização e dados reais; nada de placeholder).
9. FAQ, faixa de CTA, formulário de orçamento, botão flutuante de WhatsApp e rodapé completo.

**Critérios para aprovar um candidato**
- Leve (sem bibliotecas pesadas), acessível (teclado, foco visível, contraste AA) e responsivo.
- Combina com a paleta do logo e passa credibilidade B2B (nada de visual de "startup de IA").
- Licença permite uso comercial.
- Não usa dados ou textos de exemplo que possam ir parar no ar por engano.
- Não deixa o site parecido com o da PJ.

**Como coletar (feito pelo Claude Code, decidido pelo dono)**
0. Comece pelas referências que o dono mandar (seção 9.1.1). O que ele enviar tem prioridade sobre as suas buscas.
1. Para cada item acima, pesquisar e salvar em `design/referencias/<item>/` um arquivo `candidatos.md` com: nome, link, por que serve, adaptação necessária e licença.
2. Tirar um screenshot de cada candidato (desktop e celular) com `playwright-cli`.
3. Gerar uma página `design/referencias/index.html` com todos os screenshots lado a lado para o dono escolher.
4. Só depois da escolha, adaptar o componente ao projeto. Nunca copiar um template inteiro, e não adicionar dependência sem aprovação.

## 10. Como trabalhar
1. Antes de codar, apresente um plano curto e espere aprovação.
2. Faça por fases, nesta ordem: (a) extração de dados e imagens, (b) proposta visual (seção 9.2) e depois estrutura e componentes, (c) páginas, (d) SEO, (e) segurança, (f) testes, (g) publicação. Status informado pelo dono: a próxima fase é a (b); confirme no `PENDENCIAS.md` que a (a) foi concluída.
3. Rode `npm run build` e corrija todos os erros e avisos.
4. Checagens finais: Lighthouse, validação de HTML, checagem de links quebrados, teste dos cabeçalhos de segurança, teste do formulário, teste em celular.
5. Entregue um resumo do que foi feito e uma lista do que depende do dono.

## 11. Pendências com o dono
Estas respostas mudam o que o Claude Code vai construir. O dono responde quando tiver:
- [ ] **WhatsApp da PLAS** (com DDD), para o botão de orçamento
- [ ] **Plano da Hostinger**: roda PHP? Isso decide o formulário de orçamento (envio por PHP na própria hospedagem ou serviço externo). Conferir no painel da Hostinger (hPanel) o plano contratado e as configurações de PHP. Confirmar também se o `.htaccess` funciona.
- [ ] **CNPJ e endereço completo**, para o rodapé, o Google Meu Negócio e os dados estruturados
- [ ] **Logo em alta resolução**, de preferência em SVG (se só houver PNG, informar o tamanho)
- [ ] URL do **Profitize** (templates), se quiser que seja usado como fonte
- [ ] Confirmar as medidas marcadas como "confirmar" (Cestos de Pão e Bandeja 04)
- [ ] Lista completa de produtos (o site antigo corta a lista)
- [ ] Autorização para usar Google Analytics (se desejado)
- [ ] Colocar o arquivo `e597fed1-skills-main_2.zip` na pasta do projeto
