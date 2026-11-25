# Pendências da extração (fase a)

Gerado por `scripts/pendencias.py` a partir dos dados do site antigo. **Nada aqui foi corrigido por conta própria.**
No site novo, medidas com erro de digitação aparecem como "a confirmar" até o dono responder.

Resumo: **159 produtos**, **343 fotos da PLAS**, **147 fotos de produto da PJ** (135 produtos da PJ associados).

## 1. Medidas com erro de digitação ou sem unidade

| Produto | Problema |
|---|---|
| Cesto de Pão 51 litros | Medidas Externa: "16,5 x 59,8 x 70,6 cm" está com erro de digitação (provável: 16,5 x 59,8 x 70,6 cm) |
| Cesto de Pão 40 litros | Medidas Externa: "15,5 x 58 x 66,5 cm" está com erro de digitação (provável: 15,5 x 58 x 66,5 cm) |
| Espreguiçadeira Miami Club | Medidas: "28,0×67,0×190,0" sem unidade (provavelmente cm) |
| Espreguiçadeira Miami | Medidas: "28,0×67,0×190,0" sem unidade (provavelmente cm) |
| Pá Catabituca em Aço Inox | Medidas (caçamba aberta): "82,0, x 22,8 x 11,7 cm" está com erro de digitação (provável: 82 x 22,8 x 11,7 cm) |
| Pallet Contenção 4 Tambores 150 litros | Comprimento com Rampa: "206,90" é um número só, sem unidade |
| Lixeira 100 litros com pedal | Medidas: "92,5 x 42,5 x 59,5 cm" está com erro de digitação (provável: 92,5 x 42,5 x 59,5 cm) |

## 2. Cubagem (m³/unidade) e volume que não batem com as medidas

Conferido em todos os produtos que informam cubagem: m³ = altura x largura x comprimento das medidas externas. Tolerância de 15%.

| Produto | Problema |
|---|---|
| Cesto de Pão 51 litros | cubagem informada 0,5495 m³ não bate com medidas externas prováveis 16,5 x 59,8 x 70,6 cm (0,0697 m³) |
| Bandeja 18 | volume 18 L vs medidas internas 8,5 x 34 x 53 cm (~15,3 L) |
| Bandeja 04 | cubagem informada 0,088 m³ não bate com medidas externas 7 x 30 x 42 cm (0,0088 m³) |

## 3. Pesos com número ambíguo

| Produto | Problema |
|---|---|
| Pallet Contenção 4 Tambores 150 litros | Peso com Rampa: "42.300 Kg." — ponto pode ser milhar ou decimal (provável 42,3 kg); confirmar |
| Lixeira Rotomoldada 100 litros com tampa basculante | Peso: "2.200 Kg." — ponto pode ser milhar ou decimal (provável 2,2 kg); confirmar |

## 4. Categoria

Produtos sem categoria no site antigo receberam uma categoria provisória pelo nome. Confirmar.

| Produto | Problema |
|---|---|
| Caixa Fechada 50 litros | sem categoria no site antigo; categoria provisória atribuída |
| Caixa Fechada 74 litros | sem categoria no site antigo; categoria provisória atribuída |
| Mesa Plástica Retangular | sem categoria no site antigo; categoria provisória atribuída |
| Banco de Plástico Comfort | sem categoria no site antigo; categoria provisória atribuída |
| Pá Plástica com Cabo e Tampa Plástica | sem categoria no site antigo; categoria provisória atribuída |

## 5. Produtos com o mesmo nome no site antigo

Para o cliente conseguir diferenciar, o nome exibido ganhou a capacidade ou a medida (tirada dos próprios dados). Confirmar se o dono prefere outro nome (ex.: código do fabricante).

| Produto | Problema |
|---|---|
| Cesto de Pão 51 litros | nome repetido no site antigo ("Cesto de Pão"); exibido como "Cesto de Pão 51 litros" |
| Caixa Fechada 130 litros (41 x 56 x 78 cm) | nome repetido no site antigo ("Caixa Fechada 130 litros"); exibido como "Caixa Fechada 130 litros (41 x 56 x 78 cm)" |
| Cesto de Pão 40 litros | nome repetido no site antigo ("Cesto de pão"); exibido como "Cesto de Pão 40 litros" |
| Caixa Fechada 130 litros (40,5 x 55,5 x 76 cm) | nome repetido no site antigo ("Caixa Fechada 130 litros"); exibido como "Caixa Fechada 130 litros (40,5 x 55,5 x 76 cm)" |

## 6. Dados faltando

A ficha técnica desses produtos fica sem o campo até o dono enviar o dado.

| Produto | Falta |
|---|---|
| Banqueta Plástica | medidas, peso |
| Cadeira Bistrô | peso |
| Cadeira Juvenil | peso |
| Caixa Plástica 370 litros | peso |
| Carro Coletor 370 litros | peso |
| Carro Para Caixa 180 litros | cores |
| Conjunto de Mesa e Cadeira Infantil | peso |
| Container Plástico 1000 litros | peso |
| Container Plástico 1000 litros com Pedal | peso |
| Container Plástico 660 litros | peso |
| Container Plástico 660 litros Com Pedal | peso |
| Gaveteiro 03 | peso |
| Gaveteiro 04 | peso |
| Gaveteiro 05 | peso |
| Gaveteiro 06 | peso |
| Gaveteiro 07 | peso |
| Gaveteiro 08 | peso |
| Kit Completo do Carrinho Funcional de Limpeza | medidas, peso, cores |
| Kit do Balde Espremedor | medidas, peso, cores |
| Lixeira 100 litros com tampa vai e vem | peso |
| Lixeira 25 litros com tampa vai e vem | peso |
| Lixeira 60 litros com tampa basculante | peso |
| Lixeira 60 litros com tampa vai e vem | peso |
| Lixeira Mix Inox com 2 Divisões para Coleta Seletiva | peso |
| Lixeira Mix Inox com 3 Divisões para Coleta Seletiva | peso |
| Lixeira Mix Plástica com 2 Divisões para Coleta Seletiva | peso |
| Lixeira Mix Plástica com 3 Divisões para Coleta Seletiva | peso |
| Lixeira Para Descarte de Pilhas e Baterias | peso |
| Lixeira Plástica para Descarte de Pilhas e Baterias 40 litros | peso |
| Lixeira Plástica para Descarte de Pilhas e Baterias 50 litros | peso |
| Lixeira Quadrada 100 litros com pedal e Rodas | peso |
| Lixeira Quadrada 15 litros com pedal | peso |
| Lixeira Quadrada 25 litros com pedal | peso |
| Lixeira Quadrada 30 litros com pedal | peso |
| Lixeira Quadrada 60 litros com pedal | peso |
| Lixeira Rotomoldada 100 litros com tampa basculante | peso |
| Mesa Juvenil | peso |
| Mesa Plástica Monobloco | peso |
| Mesa Plástica Redonda | peso |
| Mesa Plástica Retangular | peso |
| Poltrona com braço | peso |
| Pá Catabituca em Aço Inox | peso |
| Pá Plástica com Cabo e Tampa Plástica | peso |

## 7. Fotos

- Produtos sem foto: nenhum.
- Foto principal com menos de 768 px de largura (119 produtos). Funciona, mas fica pequena em tela grande; vale pedir fotos melhores:

  - Kit Completo do Carrinho Funcional de Limpeza (207 x 181 px)
  - Mesa Plástica Redonda (225 x 225 px)
  - Cadeira Bistrô (228 x 228 px)
  - Pá Plástica com Cabo e Tampa Plástica (277 x 281 px)
  - Cadeira Juvenil (280 x 280 px)
  - Lixeira 240 litros com pedal (280 x 280 px)
  - Lixeira plástica 240 litros (280 x 280 px)
  - Lixeira plástica 120 litros com pedal (280 x 280 px)
  - Caixa Fechada 38 litros (284 x 247 px)
  - Pallet Plástico Heavy (300 x 300 px)
  - Lixeira Mix Inox com 3 Divisões para Coleta Seletiva (400 x 400 px)
  - Lixeira Mix Inox com 2 Divisões para Coleta Seletiva (400 x 400 px)
  - Cesto de Lixo 100 litros Redondo com Pedal (400 x 400 px)
  - Caixa Plástica 370 litros (400 x 326 px)
  - Container Rotomoldado 500 litros com Pedal (400 x 400 px)
  - Container Rotomoldado 500 litros (400 x 400 px)
  - Container Rotomoldado 700 litros com Pedal (400 x 400 px)
  - Lixeira plástica 360 litros (400 x 400 px)
  - Container Rotomoldado 700 litros (400 x 400 px)
  - Container Rotomoldado 1000 litros com Pedal (400 x 400 px)
  - Container Rotomoldado 1000 litros (400 x 400 px)
  - Pallet Plástico Liso Polietileno (400 x 400 px)
  - Pallet Plástico Vazado Polietileno (400 x 400 px)
  - Estrado 50x50 cm (400 x 400 px)
  - Caixa Hortifruti Vazada 46 litros (400 x 400 px)
  - Caixa Vazada 46 litros (400 x 400 px)
  - Caixa Vazada 46 litros fundo fechado (400 x 400 px)
  - Pallet Contenção 2 Tambores 255 litros (450 x 409 px)
  - Carro Coletor 370 litros (450 x 450 px)
  - Lixeira Quadrada 25 litros com pedal (450 x 450 px)
  - Lixeira Quadrada 30 litros com pedal (450 x 450 px)
  - Caixa Fechada 46 litros (450 x 450 px)
  - Mesa Juvenil (458 x 458 px)
  - Pallet Contenção 1 Tambor 100 litros (474 x 474 px)
  - Pallet Contenção 4 Tambores 420 litros (474 x 474 px)
  - Banco de Plástico Comfort (480 x 480 px)
  - Pallet Contenção 2 Tambores 75 litros (480 x 480 px)
  - Cesto de Lixo 100 litros Redondo (480 x 480 px)
  - Pallet Contenção 4 Tambores 150 litros (480 x 480 px)
  - Cesto de Lixo 60 litros Redondo com Pedal (480 x 480 px)
  - Cesto de Lixo 60 litros Redondo (480 x 480 px)
  - Carro Cuba 430 litros (480 x 480 px)
  - Carro Cuba 180 litros (480 x 480 px)
  - Carro Para Caixa 180 litros (480 x 480 px)
  - Cesto de Lixo 23 litros com Tampa Basculante (480 x 480 px)
  - Cesto de Lixo 23 litros com Tampa Flip-Top (480 x 480 px)
  - Cesto de Lixo 23 litros (480 x 480 px)
  - Cesto de Lixo 15 litros com Tampa Basculante (480 x 480 px)
  - Cesto de Lixo 15 litros com Tampa Flip-Top (480 x 480 px)
  - Cesto de Lixo 15 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 6 Lixeiras 60 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 5 Lixeiras 60 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 4 Lixeiras 60 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 3 Lixeiras 60 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 2 Lixeiras 60 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 6 Papeleiras 50 litros (480 x 481 px)
  - Conjunto Coleta Seletiva 5 Papeleiras 50 litros (480 x 479 px)
  - Conjunto Coleta Seletiva 4 Papeleiras (480 x 480 px)
  - Conjunto Coleta Seletiva 3 Papeleiras 50 litros (480 x 480 px)
  - Conjunto Coleta Seletiva 2 Papeleiras 50 litros (480 x 479 px)
  - Lixeira plástica 120 litros (480 x 480 px)
  - Container Rotomoldado 1000 litros com Tampa Bipartida (480 x 480 px)
  - Lixeira Rotomoldada 100 litros com tampa basculante (480 x 480 px)
  - Lixeira 60 litros com tampa basculante (480 x 480 px)
  - Lixeira 100 litros com pedal e rodas (480 x 480 px)
  - Pallet Plástico Liso 6 Runners (480 x 480 px)
  - Pallet Plástico Liso 3 Runners (480 x 480 px)
  - Pallet Plástico Liso (480 x 480 px)
  - Pallet Plástico Empílhável (480 x 480 px)
  - Pallet Plástico Vazado 6 Runners (480 x 480 px)
  - Pallet Plástico Vazado 3 Runners (480 x 480 px)
  - Pallet Plástico Vazado (480 x 480 px)
  - Caixa ALC 6437 (480 x 480 px)
  - Caixa RL-KLT 6431 (480 x 480 px)
  - Caixa R-KLT 6428 (480 x 480 px)
  - Caixa RL-KLT 6421 (480 x 480 px)
  - Caixa R-KLT 4329 (480 x 480 px)
  - Estrado 41x82 cm (480 x 480 px)
  - Caixa RL-KLT4315 (480 x 480 px)
  - Caixa R-KLT 4315 (480 x 480 px)
  - Caixa Fechada 7 litros (480 x 480 px)
  - Caixa Fechada 15 litros (480 x 480 px)
  - Caixa Fechada 26 litros (480 x 480 px)
  - Caixa Fechada 36 litros (480 x 480 px)
  - Caixa Fechada 61 litros (480 x 480 px)
  - Caixa Fechada 130 litros (40,5 x 55,5 x 76 cm) (480 x 480 px)
  - Caixa Fechada 180 litros (480 x 480 px)
  - Bandeja 02 (500 x 500 px)
  - Banqueta Plástica (500 x 500 px)
  - Mesa Plástica Retangular (500 x 414 px)
  - Mesa Plástica Monobloco (500 x 667 px)
  - Caixa Fechada 70 litros (500 x 500 px)
  - Pallet Plástico KLT (500 x 500 px)
  - Tampa Caixa GLT/Pallet (500 x 500 px)
  - Lixeira 25 litros com tampa vai e vem (546 x 454 px)
  - Lixeira 60 litros com tampa vai e vem (546 x 454 px)
  - Lixeira 100 litros com tampa vai e vem (546 x 454 px)
  - Caixa Frigorífica 42 litros (546 x 454 px)
  - Caixa Vazada 33 litros (546 x 454 px)
  - Caixa Vazada 60 litros (546 x 454 px)
  - Lixeira Papeleira 50 litros com Poste (553 x 278 px)
  - Lixeira Papeleira 50 litros (553 x 278 px)
  - Lixeira 100 litros com pedal (553 x 278 px)
  - Lixeira 50 litros com pedal (553 x 278 px)
  - Lixeira 25 litros com pedal (553 x 278 px)
  - Lixeira 15 litros com pedal (553 x 278 px)
  - Caixa Fechada 03 (600 x 450 px)
  - Cesto de Pão 51 litros (600 x 450 px)
  - Caixa Fechada 130 litros (41 x 56 x 78 cm) (600 x 450 px)
  - Estrado 1060 cm (600 x 450 px)
  - Cesto supermercado (600 x 450 px)
  - Cesto de Pão 40 litros (600 x 450 px)
  - Caixa Pallet GLT (600 x 594 px)
  - Cesto Plástico Empilhável Médio (600 x 600 px)
  - Cesto Plástico Empilhável Pequeno (600 x 600 px)
  - Caixa Fechada 74 litros (613 x 613 px)
  - Espreguiçadeira Miami (700 x 700 px)
  - Caixa Vazada 64 (709 x 613 px)
  - Container Plástico 660 litros (739 x 620 px)

- Fotos cujo nome de arquivo cita outra marca ou fabricante. O briefing diz que as fotos são do dono; só confirmar se há autorização do fabricante para uso (é comum revendedor poder usar):

  - "larplasticos": Pallet Contenção 2 Tambores 75 litros, Carro Para Caixa 180 litros, Lixeira plástica 120 litros, Container Rotomoldado 1000 litros com Tampa Bipartida, Caixa Fechada 130 litros (40,5 x 55,5 x 76 cm)
  - "arcos": Poltrona com braço
  - "galia": Caixa Galia 1322
  - "maxicaixa": Caixa Pallet GLT
  - "ecopallet": Pallet Plástico Empílhável
  - "smart": Pallet Plástico Liso 6 Runners, Pallet Plástico Liso 3 Runners, Pallet Plástico Liso, Pallet Plástico Vazado 6 Runners, Pallet Plástico Vazado 3 Runners, Pallet Plástico Vazado

## 8. PJ Comercial

Produtos que existem na PJ mas **não** foram encontrados no site da PLAS. Podem ser itens que faltam no catálogo (o briefing diz que a lista do site antigo é incompleta). Não entram no site novo sem confirmação:

- **Espreguiçadeira** (`espreguicadeira`): Espreguiçadeira Cores disponíveis – Branco
- **Gaveteiro Plástico Bin Nº 9 – 50 Litros** (`gaveteiro-plastico-bin-no-9-50-litros`): Dimensões Externas 39cmx57,5cmx23cm (LarguraxComprimentoxAltura Capacidade volumétrica 50 litros Capacidade de carga por caixa 22 kg Peso 1,72 kg Cubagem por volume 0,103 m³ (8 unidades) Cores Disponíveis Polipropileno:
- **Pallet de contenção IBC 1000 Litros - 04 tambores** (`pallet-de-contencao-ibc-1000-litros-04-tambores`): IBC 1000 LITROS – 04 Tambores Largura: 2000 mm | Altura: 650 mm | Comprimento: 1500 mm Capacidades: Carga 1300 kg | Contenção 1000 L Material: PEAD ou PEMD Peso: 100 kg Cores: Amarelo Laranja Cinza

Observação: o briefing diz que a PJ não tem medidas, mas várias páginas da PJ têm. Os dados técnicos do site novo vêm só da PLAS.

## 9. Endereços (URLs) que mudaram

41 produtos tinham endereço antigo diferente do nome (ex.: o "Kit Completo do Carrinho Funcional de Limpeza" estava em `/produto/placa-sinalizadora-sem-mensagem/`). Todos ganham endereço novo pelo nome, com redirecionamento 301 do antigo (`data/redirects.json`). Só para conhecimento.

- `/produto/cesto-de-pao-2/` → `/produtos/cestos-e-gaveteiros/cesto-de-pao-51-litros/`
- `/produto/caixa-fechada-130-litros-2/` → `/produtos/caixas-plasticas/caixa-fechada-130-litros-78/`
- `/produto/cesto-de-pao/` → `/produtos/cestos-e-gaveteiros/cesto-de-pao-40-litros/`
- `/produto/conjunto-de-mesa-e-cadeira-juvenil/` → `/produtos/moveis-plasticos/mesa-juvenil/`
- `/produto/poltrona-infatil/` → `/produtos/moveis-plasticos/conjunto-de-mesa-e-cadeira-infantil/`
- `/produto/mesa-monobloco/` → `/produtos/moveis-plasticos/mesa-plastica-monobloco/`
- `/produto/banco-de-plastico-comfort-com-encosto/` → `/produtos/moveis-plasticos/banco-de-plastico-comfort/`
- `/produto/placa-sinalizadora-sem-mensagem/` → `/produtos/containers-e-carros/kit-completo-do-carrinho-funcional-de-limpeza/`
- `/produto/placa-sinalizadora-piso-escorregadio/` → `/produtos/containers-e-carros/kit-do-balde-espremedor/`
- `/produto/placa-sinalizadora-piso-molhado/` → `/produtos/lixeiras/pa-catabituca-em-aco-inox/`
- `/produto/lixeira-plastica-para-descarte-de-pilhas-e-baterias/` → `/produtos/lixeiras/lixeira-plastica-para-descarte-de-pilhas-e-baterias-40-litros/`
- `/produto/pallet-contencao-2-tambores-255/` → `/produtos/pallets/pallet-contencao-2-tambores-255-litros/`
- `/produto/cesto-de-lixo-60-litros-redonda-com-pedal/` → `/produtos/lixeiras/cesto-de-lixo-60-litros-redondo-com-pedal/`
- `/produto/lixeira-quadrada-25-litros-c-pedal/` → `/produtos/lixeiras/lixeira-quadrada-25-litros-com-pedal/`
- `/produto/lixeira-quadrada-100-litros-c-pedal-e-rodas/` → `/produtos/lixeiras/lixeira-quadrada-100-litros-com-pedal-e-rodas/`
- `/produto/lixeira-quadrada-60-litros-c-pedal/` → `/produtos/lixeiras/lixeira-quadrada-60-litros-com-pedal/`
- `/produto/lixeira-quadrada-30-litros-c-pedal/` → `/produtos/lixeiras/lixeira-quadrada-30-litros-com-pedal/`
- `/produto/lixeira-quadrada-15-litros-c-pedal/` → `/produtos/lixeiras/lixeira-quadrada-15-litros-com-pedal/`
- `/produto/conjunto-coleta-seletiva-2-lixeiras-60-litros-2/` → `/produtos/lixeiras/conjunto-coleta-seletiva-3-lixeiras-60-litros/`
- `/produto/lixeira-papeleira-50-litros-c-poste/` → `/produtos/lixeiras/lixeira-papeleira-50-litros-com-poste/`
- `/produto/lixeira-240-litros-c-pedal/` → `/produtos/lixeiras/lixeira-240-litros-com-pedal/`
- `/produto/lixeira-plastica-120-litros-c-pedal/` → `/produtos/lixeiras/lixeira-plastica-120-litros-com-pedal/`
- `/produto/cesto-plastico-50-litros-c-tampa-vai-vem/` → `/produtos/lixeiras/lixeira-plastica-120-litros/`
- `/produto/container-1000-litros-com-tampa-bipartida/` → `/produtos/containers-e-carros/container-rotomoldado-1000-litros-com-tampa-bipartida/`
- `/produto/container-plasticos-1000-litros-com-pedal/` → `/produtos/containers-e-carros/container-plastico-1000-litros-com-pedal/`
- `/produto/lixeira-100-litros-c-tampa-basculante/` → `/produtos/lixeiras/lixeira-rotomoldada-100-litros-com-tampa-basculante/`
- `/produto/lixeira-60-litros-c-tampa-baculante/` → `/produtos/lixeiras/lixeira-60-litros-com-tampa-basculante/`
- `/produto/lixeira-25-litros-c-tampa-vai-vem/` → `/produtos/lixeiras/lixeira-25-litros-com-tampa-vai-e-vem/`
- `/produto/lixeira-60-litros-c-tampa-vai-vem/` → `/produtos/lixeiras/lixeira-60-litros-com-tampa-vai-e-vem/`
- `/produto/lixeira-c-tampa-vai-vem-100-litros/` → `/produtos/lixeiras/lixeira-100-litros-com-tampa-vai-e-vem/`
- `/produto/lixeira-100-litros-c-pedal-e-rodas/` → `/produtos/lixeiras/lixeira-100-litros-com-pedal-e-rodas/`
- `/produto/lixeira-100-litros-c-pedal/` → `/produtos/lixeiras/lixeira-100-litros-com-pedal/`
- `/produto/lixeira-50-litros-c-pedal/` → `/produtos/lixeiras/lixeira-50-litros-com-pedal/`
- `/produto/lixeira-25-litros-c-pedal/` → `/produtos/lixeiras/lixeira-25-litros-com-pedal/`
- `/produto/lixeira-15-litros-c-pedal/` → `/produtos/lixeiras/lixeira-15-litros-com-pedal/`
- `/produto/pallet-plastico-liso-6-runerrs/` → `/produtos/pallets/pallet-plastico-liso-6-runners/`
- `/produto/caixa-rl-klt3147/` → `/produtos/caixas-plasticas/caixa-rl-klt-3147/`
- `/produto/caixa-frigorifico-42-litros/` → `/produtos/caixas-plasticas/caixa-frigorifica-42-litros/`
- `/produto/caixa-vazada-46-litros-fundo-fechadoduraflex-fiberglass-hood-2/` → `/produtos/caixas-plasticas/caixa-vazada-46-litros-fundo-fechado/`
- `/produto/caixa-fechada-42-litros/` → `/produtos/caixas-plasticas/caixa-fechada-4-2-litros/`
- `/produto/caixa-fechada-130-litros/` → `/produtos/caixas-plasticas/caixa-fechada-130-litros-76/`

## 10. Pendências gerais com o dono (do briefing)

- [ ] CNPJ da PLAS (aparece no rodapé; não consta no site antigo)
- [ ] Número de WhatsApp da PLAS
- [ ] Endereço completo (o site antigo só diz Santo André/SP)
- [ ] Confirmar as medidas das seções 1 a 3
- [ ] Lista completa de produtos (ver também a seção 8)
- [ ] Logo em alta resolução (de preferência SVG). O logo atual (PNG 500 px) é todo em cinza-grafite (#484343), sem cor: a cor de destaque do site será uma proposta, a aprovar
- [ ] Plano da Hostinger (suporta PHP e `.htaccess`?)
- [ ] Autorização para usar Google Analytics (se desejado)
