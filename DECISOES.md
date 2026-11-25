# Decisões do projeto

Registro de decisões do dono e de conflitos entre skills (briefing, seção 9.1, regra b).

## Decisões do dono

| Data | Decisão |
|---|---|
| 25/11/2026 | Medidas, cubagens e pesos com erro ou ambíguos vão para o site **como estão escritos no site antigo**. O dono corrige depois, se for o caso. Na prática: a ficha técnica mostra o texto original de cada linha (`specs` em `data/products.json`), sem "consertar" nada. |
| 25/11/2026 | Os 2 produtos que só existem na PJ (Gaveteiro Bin Nº 9 e Pallet de Contenção IBC) **entram no site**, com os dados da página da PJ. |
| 25/11/2026 | Produtos sem peso ficam **sem peso**: a linha não aparece na ficha técnica. |
| 25/11/2026 | O uso de **todas as fotos** está liberado, inclusive as que têm nome de fabricante no arquivo. |
| 25/11/2026 | O dono **não tem referências externas** e aprovou a recomendação de estilo (`design/recomendacao.md`): "pode seguir com as suas ideias, qualquer coisa alteramos depois". |
| 25/11/2026 | Cor de destaque: **azul** (#1F5FA8). |
| 25/11/2026 | Skills da Emil instaladas a partir do zip: só `emil-design-eng`, `review-animations`, `animation-performance`, `break-ui` e `prototype` (as de Swift, Expo e mobile ficaram de fora, como pede o briefing). |

## Decisões técnicas da fase (a)

| Decisão | Por quê |
|---|---|
| Endereços novos dos produtos gerados a partir do nome, com 301 do endereço antigo | 39 produtos tinham endereço antigo que não correspondia ao nome (ex.: o kit do carrinho de limpeza em `/placa-sinalizadora-sem-mensagem/`). |
| Produtos homônimos ganham a capacidade ou a medida no nome | Dois "Caixa Fechada 130 litros" e dois "Cesto de Pão" diferentes. O dado acrescentado vem do próprio produto. |
| 46 URLs do site antigo respondem 410 (removida) | São páginas de demonstração do tema WordPress indexadas no Google ("fones Bluetooth", "auto peças"). 410 faz o Google tirá-las do índice mais rápido do que 404. |
| Dependências com versão fixa, publicadas há 2 semanas ou mais, e `ignore-scripts=true` no `.npmrc` | Skill `security-and-hardening`: cadeia de suprimentos. |

## Conflitos entre skills

Ordem de precedência do briefing: `frontend-design` > `design-taste-frontend` > `web-design-guidelines` > `impeccable` > Emil > `playwright-cli` > `break-ui`. O briefing e a regra "desempenho, acessibilidade, SEO e segurança vencem a estética" ficam acima de todas.

| Conflito | Decisão |
|---|---|
| `design-taste-frontend`, regra 9: contatos em `.example`, sem número de telefone real, sem CNPJ, sem número no endereço | **Vale o briefing.** Essa regra é para páginas de demonstração. Aqui é o site real da empresa: telefone, e-mail, CNPJ e endereço reais (briefing, seções 2 e 7: `LocalBusiness`). |
| `design-taste-frontend`: "sorteie a paleta e o layout, nunca escolha por gosto" | **Vale o briefing (9.1.1).** Quem decide o visual é o dono, a partir das referências dele. O sorteio da skill pode, no máximo, gerar alternativas para a proposta. |
| `design-taste-frontend`, regra 1: "nenhuma legenda sob imagens" | Nome e dados do produto no card são rótulo de catálogo, não legenda explicativa. Ficam. A regra vale para fotos de contexto (sem legenda decorativa). |
| `design-taste-frontend`, regra 3: "uma seção por tela" | Vale na home e nas páginas de setor. **Não vale** no catálogo e na ficha técnica, que são telas de consulta (modo "Operate/Read" da `impeccable`): densidade de informação vence. |
| `design-taste-frontend`: "fotos substitutas de banco de imagens quando o cliente não tem" | Só com aprovação do dono e sempre identificadas como ilustrativas. Nunca passar foto de banco como produto ou cliente da PLAS. |
| `impeccable`: o comando `impeccable context` baixa um binário na primeira execução | Não rodar sem necessidade. Ler `PRODUCT.md` e `DESIGN.md` direto (caminho previsto pela própria skill quando o lançador não roda). |
| `design-taste-frontend` instala um gancho (hook) de checagem ao encerrar | Aceito quando a skill estiver em uso nas fases (b) e (c). As checagens dele que conflitam com as decisões acima são registradas como exceção (`.taste-skill/waivers.json`), com o motivo. |

## Skills por etapa (no máximo duas de design por etapa)

| Etapa | Skills de design |
|---|---|
| (b) Recomendação e proposta visual | `frontend-design` + `design-taste-frontend` (protótipos com o `prototype` da Emil, que é ferramenta de comparação, não direção de design) |
| (b) Estrutura e componentes | `frontend-design` + `web-design-guidelines` |
| (c) Páginas | `frontend-design` + `web-design-guidelines`; `impeccable` só na revisão final |
| Movimento (quando houver) | `emil-design-eng` + `review-animations` |
| Testes | `playwright-cli` e `break-ui` (não são de design) |
