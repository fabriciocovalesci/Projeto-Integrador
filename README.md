# Cafeteria *Return my coffee*

## Objetivo inicial do projeto

Objetivo inicial do projeto é desenvolver um site direcionado a cafeterias, onde os clientes fazem seus pedidos.
Cliente ao se sentar na mesa, precisa apenas escanear um QR Code com seu celular e partir dai será direcionado a uma página web, ele efetuara um cadastro com informações pessoais e enviara uma foto, a partir dai ele mesmo fará seu pedido, por meio de um cardápio online.
O restaurante também contara com um site institucional, como meio de divulgação de seus serviços digitais.
Haverá uma página destinada apenas para fins administrativos, onde apenas o proprietário e funcionários teriam acesso, cada usuário tera restrinções conforme cargo exercido.

Projeto será dividido em algumas partes para melhor entendimento.

**- Site institucional**

**- Cadastro e solicitação de pedidos**

**- Página administrativa**

## Funcionabilidades Atendidas

1. ### **Site da empresa**

   1. Menu para navegação dentro do site.
      1. Inicio.
      2. A Empresa.
      3. O Café.
      4. Localização.
      5. Contato.
      6. Login.
         1. Descrição da empresa, seus objetivos.
         2. Informações de contato  e localização.
         3. Fotos com descrições dos produtos.
         4. Formulário para usuários enviar mensagens.
         5. Login será *apenas para funcionários, serão direcionados para página admistrativa do site

2. ### **Cadastro de novos cliente**

   1. Sistema irá pergunta se cliente já está cadastrado, caso não tiver, será direcionado para o cadastro, as seguintes informações serão solicitadas:
      1. Nome
      2. telefone
      3. email
      4. endereço
      5. sexo
      6. data de nascimento
      7. foto para perfil
      8. senha para acesso
   
   2. Caso cliente ja possuir cadastro ele faz o login
   3. Após o login o sistema exibe a última compra efetuada, se caso houver
   4. Um menu na barra superior com as seguintes funções
      1. Edita perfil
      2. Café
      3. Lanches
      4. Meu Café Favorito
         1. No sub menu *Edita perfil* o usuário pode editar seu perfil
         2. No sub menu *Café*, exibe o cardapio com todos tipo de cafés disponiveis, com foto, descrição e preço.
         3. No sub menu *Lanches*, exibe o cardapio com todos os lanches disponiveis, com foto, descrição e preço.
         4. No sub menu *Meu Café Favorito*, pode se colocar um café ou lanche como favorito.

3. ### **Página Administrativa**


   1. Um sub menu na barra superior com as seguintes funções
      1. Meu Perfil
      2. Estoque
      3. Caixa
      4. Clientes
      5. Criar novo Funcionário
      6. Criar cargo para funcionário
      7. Imagens da cafeteria
         1. No sub menu *Meu Perfil* o usuário pode editar seu perfil
         2. No sub menu *Estoque* o funcionário pode consulta o estoque ou adiciona itens
         3. No sub menu *Caixa* o administrador pode verificar as vendas diárias, semanais, mensais.
            1. Se o funcionário está habilitado para trabalhar como caixa, ele pode realizar os pagamentos diários da cafeteria.
         4. No sub menu *Clientes* o administrador pode verificar quantos clientes fizeram compras diariamente, podera filtar por sexo, idade, hora de maior pedidos, tudo isso para melhorar o atendimento ou até mesmo o sistema. Também pode ajudar a criar campanhas de marketing especificos conforme com base nos pedidos dos usuários cadastrados.
         5. No sub menu *Criar novo Funcionário* o administrador pode criar novo funcionário especificando o cargo, assim o funcionário terá acesso apenas nesta area do sistema.
            1. **Cadastro de novo funcionário**
               1. Nome
               2. telefone
               3. email
               4. endereço
               5. sexo
               6. data de nascimento
               7. foto para perfil
               8. senha para acesso
         6. No sub menu *Criar cargo para funcionário* especificaria um cargo para funcionário, como caixa, estoque.
         7. No sub menu *Imagens da cafeteria* o administrador tem acesso a camera de segurança de dentro do estabelecimento, esta mesma camera identifica os clientes.


## Funcionabilidades Não Atendidas


1. ### **Funcionabilidades de pontos**

Com base nos pedidos do usuário poderia se criar um sistema de pontos, isso seria havaliado da seguinte forma:

- Cliente diário: se realizar pedidos todos dias, seria concedidos pontos, que podem ser convertidos em descontos maiores.
  
- Cliente 1 vez na semana: se realiar pedidos ao menos uma vez na semana, receberia pontos que poderia ser convertido em desconto.

2. ### **Sub menus da página administrativa**

- Poderá não ser implementada esta funcionabilidade.

- Criação de funcionário poderá não ser implementada.

- Criação de cargo para o funcionário poderá não ser implementada.

- Sub menu *Clientes* na página adminstrativa poderá não ser implementada.


# Tecnologias que serão utilizadas
