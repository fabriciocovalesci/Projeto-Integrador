# Cafeteria *Coffee Break*

## Objetivo inicial do projeto

Na busca por um atendimento mais eficiente, foi proposto desenvolver um sistema dando mais autonomia para o cliente, assim ele mesmo faz seus pedidos apenas com o proprio celular.

Cliente ao se sentar na mesa, precisa apenas escanear um QR Code com seu celular e partir dai será direcionado a uma página web, ele irá criar uma conta com suas informações pessoais, a partir dai ele mesmo fará seu pedido, por meio de um cardapio online. 

A cafeteria também contara com um site institucional, para ter maior visibilidade na internet, com finalidade de conquistar mais clientes.

### Um deploy inicial já foi realizado, e pode ser acessado neste [Link](https://cafefrontend.herokuapp.com/#/)

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
         5. Login será *apenas para funcionários, serão direcionados para página admistrativa do site.

2. ### **Cadastro de novos cliente** 

   1. Sistema irá pergunta se cliente já está cadastrado, caso não tiver, será direcionado para o cadastro, as seguintes informações serão solicitadas:
      1. Nome.
      2. telefone.
      3. email.
      4. endereço.
      5. sexo.
      6. data de nascimento.
      7. foto para perfil.
      8. senha para acesso.
   
   2. Caso cliente ja possuir cadastro ele faz o login.
   3. Após o login o sistema exibe a última compra efetuada, se caso houver.
   4. Um menu na barra superior com as seguintes funções.
      1. Edita perfil.
      2. Café.
      3. Lanches.
      4. Meu Café Favorito.
          * No sub menu *Edita perfil* o usuário pode editar seu perfil.
          * No sub menu *Café*, exibe o cardapio com todos tipo de cafés disponiveis, com foto, descrição e preço.
          * No sub menu *Lanches*, exibe o cardapio com todos os lanches disponiveis, com foto, descrição e preço.
          * No sub menu *Meu Café Favorito*, pode se colocar um café ou lanche como favorito.

3. ### **Página Administrativa**


   1. Um sub menu na barra superior com as seguintes funções.
      1. Meu Perfil.
      2. Estoque.
      3. Caixa.
      4. Clientes.
      5. Criar novo Funcionário.
      6. Criar cargo para funcionário.
      7. Imagens da cafeteria.
         * No sub menu *Meu Perfil* o usuário pode editar seu perfil.
         * No sub menu *Estoque* o funcionário pode consulta o estoque ou adiciona itens.
         * No sub menu *Caixa* o administrador pode verificar as vendas diárias, semanais, mensais.
         * Se o funcionário está habilitado para trabalhar como caixa, ele pode realizar os pagamentos diários da cafeteria.
         * No sub menu *Clientes* o administrador pode verificar quantos clientes fizeram compras diariamente, podera filtar por sexo, idade, hora de maior pedidos, tudo isso para melhorar o atendimento ou até mesmo o sistema. Também pode ajudar a criar campanhas de marketing especificos conforme com base nos pedidos dos usuários cadastrados.
         * No sub menu *Criar novo Funcionário* o administrador pode criar novo funcionário especificando o cargo, assim o funcionário terá acesso apenas nesta area do sistema.
            1. **Cadastro de novo funcionário**
               1. Nome.
               2. telefone.
               3. email.
               4. endereço.
               5. sexo.
               6. data de nascimento.
               7. foto para perfil.
               8. senha para acesso.
         1. No sub menu *Criar cargo para funcionário* especificaria um cargo para funcionário, como caixa, estoque.
         2. No sub menu *Imagens da cafeteria* o administrador tem acesso a camera de segurança de dentro do estabelecimento, esta mesma camera identifica os clientes.


## Funcionabilidades Não Atendidas


#### **Funcionabilidades de pontos**

Com base nos pedidos do usuário poderia se criar um sistema de pontos, isso seria havaliado da seguinte forma:

- Cliente diário: se realizar pedidos todos dias, seria concedidos pontos, que podem ser convertidos em descontos maiores.
  
- Cliente uma vez na semana: se realiar pedidos ao menos uma vez na semana, receberia pontos que poderia ser convertido em desconto.

#### **Sub menus da página administrativa**

- Poderá não ser implementada esta funcionabilidade.

- Criação de funcionário poderá não ser implementada.

- Criação de cargo para o funcionário poderá não ser implementada.

- Sub menu *Clientes* na página adminstrativa poderá não ser implementada.


# Tecnologias que serão utilizadas

Para desenvolvimento do site serão utilizados as seguintes tecnologias:

## Back-end

- Django
- Django REST framework
- GraphQL

## Front-end

- Vue.js
- HTML
- CSS
- JavaScript

## Banco de Dados

- PostgreSQL

## Platform as a Service - PaaS

- Heroku
