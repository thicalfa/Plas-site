# Mudança da PLAS para a Hostinger: passo a passo

Guia para o dono da PLAS. Objetivo: tirar o site e os e-mails da hospedagem antiga e colocar tudo na conta Hostinger (plano **Business Web Hosting**), **sem o site nem os e-mails saírem do ar**.

> **Regra de ouro:** não cancele nada na hospedagem antiga até a **Etapa 8**. Enquanto ela estiver paga, sempre dá para voltar atrás.
>
> **Senhas:** você digita as senhas nos sites oficiais. Não mande senhas pelo chat nem por e-mail para ninguém.
>
> Os nomes de menus podem mudar um pouco com atualizações dos painéis. Se algo não bater, mande um print que eu indico o caminho.

---

## Etapa 0: as contas de que você vai precisar

| # | Conta | Para quê | Como conferir se você tem |
|---|---|---|---|
| 1 | **Hostinger** (já tem) | Onde o site e os e-mails novos vão ficar | Você já entra no hPanel |
| 2 | **Registro.br** | É onde o domínio `plasdistribuidora.com.br` está registrado. Lá você diz para onde o domínio "aponta" | Entre em **registro.br**, clique em **Entrar** e use o CPF/CNPJ do titular do domínio (ou o ID de usuário) e a senha. Se não souber, veja o quadro abaixo |
| 3 | **Painel da hospedagem antiga** | Listar os e-mails, copiar as configurações e fazer backup | O login que vocês usam hoje para o painel (cPanel, Plesk ou painel próprio da empresa) |
| 4 | **Senha de cada e-mail da PLAS** | Para importar as mensagens antigas para a Hostinger | Quem usa cada e-mail sabe a senha; se ninguém souber, dá para trocar no painel antigo (Etapa 1) |
| 5 | **GitHub** (já tem) | O site novo fica lá; a Hostinger puxa de lá | Repositório `thicalfa/plas-site` |
| 6 | **Conta Google** (pode ser a mesma do Gmail da empresa) | Depois da mudança: Google Search Console e Perfil da Empresa no Google | Qualquer conta Google serve; de preferência uma da empresa, não pessoal |

### Não sabe o login do Registro.br?
1. Em **registro.br**, pesquise `plasdistribuidora.com.br` na busca da página inicial. O resultado mostra o **titular** (pessoa ou empresa) e a data de expiração.
2. Se o titular for a PLAS ou o dono: em **Entrar**, use **Esqueci minha senha**. O código chega no e-mail cadastrado no domínio.
3. Se o titular for **outra pessoa ou empresa** (por exemplo, a agência ou o técnico que fez o site antigo), peça a ela a **transferência de titularidade** para a PLAS antes de tudo. É grátis e é feita no próprio Registro.br. O domínio precisa estar no nome da empresa.
4. Se o domínio estiver perto de expirar, renove antes de começar.

---

## Etapa 1: inventário na hospedagem antiga (uns 30 minutos)

Entre no painel da hospedagem antiga e anote/printe:

1. **Contas de e-mail:** a lista completa (ex.: `vendas@`, `contato@`, `financeiro@`), o tamanho de cada caixa e quem usa cada uma. Anote também **redirecionamentos** ("encaminhadores") e **respostas automáticas**, se houver.
2. **Senhas dos e-mails:** confirme com cada pessoa que ela sabe a senha. Se ninguém souber, troque a senha no painel antigo e anote em local seguro.
3. **Registros DNS:** procure a tela **Zona DNS**, **Editor de zona** ou **DNS**. Tire **print da lista inteira**. É importante por causa de registros que talvez existam e não podem sumir: verificação do Google, de Facebook, de nota fiscal ou outros sistemas (registros do tipo **TXT** e **CNAME**).
4. **Backup do site antigo (WordPress):** no painel, procure **Backup** e baixe um backup completo (arquivos + banco de dados). Guarde no computador ou no Google Drive. Não vamos usar, é só segurança.
5. **Backup dos e-mails** (recomendado): se o painel tiver backup de e-mail, baixe também.
6. Anote **o nome da empresa de hospedagem antiga** e **a data de renovação/vencimento** do plano.

Me mande: o nome da hospedagem antiga, a lista de e-mails e o print do DNS (sem senhas).

---

## Etapa 2: adicionar o domínio na Hostinger (uns 10 minutos)

1. No hPanel, menu da esquerda, clique em **Sites**.
2. Clique em **Adicionar site** (ou **Criar ou migrar um site**).
3. Escolha a opção de **site vazio / personalizado** (não escolha WordPress nem o Criador com IA).
4. Quando pedir o domínio, escolha **usar um domínio que já tenho** e digite `plasdistribuidora.com.br`.
5. Se ele perguntar se quer apontar o domínio agora, **diga que faz isso depois**. Não troque nada no Registro.br ainda.
6. Ao final, o site aparece na lista de **Sites** com um aviso de que o domínio ainda não aponta para a Hostinger. **Isso é normal nesta etapa.**

O site da PJ continua igual. Cada site do plano fica separado.

---

## Etapa 3: criar os e-mails na Hostinger (uns 15 minutos)

1. No hPanel, menu da esquerda, clique em **E-mails**.
2. Escolha o domínio `plasdistribuidora.com.br` e ative o e-mail incluso no plano.
3. Crie **as mesmas contas** que existem hoje (lista da Etapa 1), com o mesmo nome. A senha pode ser nova; anote em local seguro.
4. Refaça os **redirecionamentos** e as **respostas automáticas**, se existiam.
5. Ainda **não** importe as mensagens antigas (isso é a Etapa 6).

Os e-mails novos ainda não recebem nada: o domínio continua apontando para a hospedagem antiga, então nada muda para quem usa o e-mail hoje.

---

## Etapa 4: o site novo entra no ar num endereço de teste (Claude faz, você aprova)

1. No hPanel, em **Sites → plasdistribuidora.com.br → Avançado → Git**, conectamos o repositório `thicalfa/plas-site`. Eu te passo os campos exatos na hora.
2. A Hostinger mostra um **endereço provisório** para ver o site antes da virada.
3. Testamos tudo nesse endereço: páginas, fotos, formulário de orçamento (enviando para o e-mail novo), WhatsApp.
4. Você aprova.

---

## Etapa 5: a virada no Registro.br (5 minutos de cliques + espera)

Escolha um dia útil de manhã, para dar tempo de acompanhar.

1. No hPanel, em **Domínios** (ou no aviso do site `plasdistribuidora.com.br`), a Hostinger mostra os **dois servidores DNS** dela. Normalmente são `ns1.dns-parking.com` e `ns2.dns-parking.com`; **use os que o seu painel mostrar**.
2. Antes de virar, na Hostinger, em **Domínios → plasdistribuidora.com.br → DNS / Nameservers**, recrie os registros **TXT** e **CNAME** especiais que você printou na Etapa 1 (verificação do Google, sistemas de nota fiscal etc.). Os de e-mail e site a Hostinger já cria sozinha. Me mande o print se tiver dúvida sobre algum.
3. Entre no **registro.br** e clique no domínio `plasdistribuidora.com.br`.
4. Na seção **DNS**, clique em **Alterar servidores DNS**.
5. Apague os servidores antigos e coloque os dois da Hostinger. Salve.
6. **Espere.** A mudança costuma valer em algumas horas, mas pode levar até 48 horas. Nesse intervalo, alguns visitantes veem o site antigo e outros o novo. É normal.

Durante a espera, alguns e-mails ainda podem chegar na caixa antiga. Por isso a importação (Etapa 6) só acontece depois.

---

## Etapa 6: trazer os e-mails antigos (1 a 2 dias depois da virada)

1. Confirme que os e-mails novos já recebem mensagens: mande um e-mail de teste de um Gmail para `vendas@plasdistribuidora.com.br` e veja se chega no **Webmail da Hostinger** (em **E-mails → Webmail**).
2. No hPanel, em **E-mails**, use a ferramenta de **importação/migração de e-mails**. Para cada conta ela pede o **servidor antigo** (ex.: `mail.plasdistribuidora.com.br` ou o endereço que a hospedagem antiga informa como "servidor IMAP"), o **e-mail** e a **senha antiga**. Ela copia todas as pastas e mensagens.
3. Configure os e-mails nos computadores e celulares com os dados da Hostinger (o painel mostra em **Configurações de conexão**). Normalmente são: entrada IMAP `imap.hostinger.com`, porta 993, SSL; saída SMTP `smtp.hostinger.com`, porta 465, SSL.

---

## Etapa 7: conferência final (Claude faz junto)

- [ ] O site abre em `https://plasdistribuidora.com.br` com cadeado (SSL). A Hostinger ativa o SSL sozinha depois da virada; se não ativar em 24 horas, ative em **Sites → Segurança → SSL**.
- [ ] Endereços antigos do Google (`/produto/...`) levam para as páginas novas (redirecionamentos 301).
- [ ] O formulário de orçamento chega em `vendas@`.
- [ ] Todas as contas de e-mail recebem e enviam.
- [ ] Mensagens antigas aparecem nas caixas novas.
- [ ] Site da PJ continua normal.
- [ ] Google Search Console: cadastrar o site e enviar o `sitemap.xml` (eu te guio).

---

## Etapa 8: cancelar a hospedagem antiga (2 semanas depois)

Só depois de tudo da Etapa 7 marcado e de **duas semanas** sem problemas:

1. Confirme que o backup da Etapa 1 está guardado.
2. Cancele o plano na hospedagem antiga. **Não cancele o domínio**: ele fica no Registro.br e só aponta para a Hostinger.

---

## Quanto tempo leva no total

| Etapa | Quem | Tempo |
|---|---|---|
| 0 e 1 | Dono | 1 hora |
| 2 e 3 | Dono (com Claude) | 30 minutos |
| 4 | Claude, dono aprova | quando o site estiver pronto |
| 5 | Dono (com Claude) | 5 minutos + até 48 h de espera |
| 6 | Dono (com Claude) | 30 minutos |
| 7 | Juntos | 30 minutos |
| 8 | Dono | 10 minutos, 2 semanas depois |
