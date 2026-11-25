# Proposta visual: PLAS Distribuidora

Briefing, seção 9.2. Base: `design/recomendacao.md`, aprovada pelo dono em 25/11/2026 ("pode seguir com as suas ideias"), com **azul como destaque**. O dono não enviou referências externas.

Protótipo navegável: `design/prototipos/hero/index.html` (teclas 1, 2 e 3 trocam a variação). Screenshots em `design/prototipos/hero/screenshots/`.

## Paleta

| Nome | Hex | Uso | Contraste |
|---|---|---|---|
| Grafite (do logo) | #484343 | bordas de botão, ícones | 9,7:1 sobre branco |
| Tinta | #2B2727 | títulos, faixa escura | 14,6:1 sobre branco |
| Texto | #3D3838 | texto corrido | 11,6:1 sobre branco |
| Texto secundário | #625C5C | legendas, contagens | 6,5:1 sobre branco (AA) |
| Concreto | #EDEBEA / #F6F5F4 | fundos de seção | |
| Linha | #D9D5D3 | bordas de cartão | |
| **Azul (destaque)** | **#1F5FA8** | botão "Pedir orçamento", links, cotas | 6,5:1 com texto branco (AA) |
| Azul escuro | #174A85 | hover do botão | |

O azul é o mesmo tom das caixas KLT que aparecem nas fotos: a cor da marca nasce do próprio produto. Fora o azul, o site é neutro (branco, concreto e grafite), para as fotos coloridas dos produtos (amarelo, verde, azul, preto) aparecerem sem disputa.

## Tipografia (2 famílias, hospedadas no site, `font-display: swap`)

- **Barlow Semi Condensed 600/700**: títulos, nomes de produto, números. Desenho de sinalização rodoviária e industrial; semicondensada, cabe nome longo de produto em uma linha.
- **Source Sans 3 (variável)**: texto, menus, fichas técnicas. Números tabulares nas tabelas de medidas.
- Escala de 1,25: 16 / 20 / 25 / 31 / 39 / 49 / 61 px. Texto corrido em 17 px, linha 1,55, até ~70 caracteres.
- Sem rótulos em caixa alta e sem palavra destacada em cor no meio do título.
- Peso das fontes: cerca de 25 KB (Barlow) + 40 KB (Source Sans) em WOFF2.

## Grid e layout

- Largura máxima 1200 px, margem lateral de 16 a 40 px, grid de 12 colunas no desktop e 1 coluna no celular.
- Raio de 6 px em tudo (botões, cartões); bordas finas no lugar de sombras.
- **Fotos padronizadas automaticamente:** margem branca recortada e produto centralizado num quadrado com a mesma folga. Assim caixa, lixeira e cadeira aparecem do mesmo tamanho no cartão (ver protótipo "Catálogo").

### Home (de cima para baixo)

```
┌───────────────────────────────────────────────────────────────┐
│ logo  Produtos Setores Sobre Contato   (11) 4421-1714 [Pedir orçamento] │  cabeçalho fixo
├───────────────────────────────────────────────────────────────┤
│ HERO (uma das 3 variações abaixo)                              │
├───────────────────────────────────────────────────────────────┤
│ Categorias: 8 cartões com foto e contagem                      │  (se o hero não for o "Catálogo")
├───────────────────────────────────────────────────────────────┤
│ Setores: hospitais, hotéis, supermercados, hortifrutis,        │
│ indústrias, logística (lista com os produtos de cada um)       │
├───────────────────────────────────────────────────────────────┤
│ Produtos em destaque: 8 cartões com foto, nome e medidas       │
├───────────────────────────────────────────────────────────────┤
│ Por que a PLAS: só fatos confirmados pelo dono                 │  (prazo, região, atendimento)
├───────────────────────────────────────────────────────────────┤
│ Faixa de orçamento: formulário curto + WhatsApp                │  fundo tinta
├───────────────────────────────────────────────────────────────┤
│ Rodapé: categorias, setores, contato, CNPJ, endereço, redes    │
└───────────────────────────────────────────────────────────────┘
                                             [WhatsApp] flutuante
```

## As 3 variações do hero

| # | Variação | Eixo | Quando é a melhor escolha | Custo |
|---|---|---|---|---|
| 1 | **Catálogo** | Navegação primeiro: a primeira tela já é a prateleira das 8 categorias | O cliente chega sabendo o que procura (caixa, lixeira, pallet) e quer ir direto | Menos marcante; parece mais "loja" |
| 2 | **Ficha técnica** | Um produto grande, com as medidas desenhadas sobre a foto | Mostra de cara o diferencial (medidas de verdade) e é o visual mais memorável | O produto da foto vira "o produto da PLAS"; as categorias ficam para a seção seguinte |
| 3 | **Setores** | Público primeiro: fundo grafite e a lista de setores | Quem compra para hospital ou hotel se reconhece na hora | Fundo escuro pesa mais; a lista precisa estar certa (o dono deve validar os produtos de cada setor) |

Movimento (as três): a primeira tela entra uma vez ao carregar (fade + 10 px, 520 ms). Na "Ficha técnica" as cotas se desenham uma vez. Cartões sobem 2 px no hover e o botão afunda levemente ao clicar. Tudo desligado com "reduzir movimento".

## O que vem de cada skill

- `frontend-design`: um único elemento marcante por página (as cotas desenhadas, na variação 2), o resto quieto; tipografia escolhida para o assunto (sinalização industrial).
- `design-taste-frontend`: foto real do produto em toda tela, título que diz o que se vende e para quem, um fato concreto na primeira tela (161 produtos, Santo André), sem efeito de fundo.
- Emil (`prototype`, `emil-design-eng`): picker de variações, ease-out forte, animações curtas, `:active` nos botões.
