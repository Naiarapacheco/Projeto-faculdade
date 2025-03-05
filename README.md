## Descrição

Este é um projeto desenvolvido com o framework Django, focado na criação e gerenciamento de conteúdo para blogs. O site permite a organização de posts em categorias, interação dos usuários através de comentários e administração do conteúdo.

## Funcionalidades

- **Cadastro de Posts**: Criação e edição de posts com título, conteúdo e categoria.
- **Sistema de Categorias**: Organização dos posts em diferentes categorias.
- **Sistema de Comentários**: Permite que os usuários interajam com os posts deixando comentários.
- **Administração Simples**: Painel administrativo integrado para facilitar a gestão de conteúdo.

## Tecnologias Utilizadas

- **Django**: Framework web utilizado para o desenvolvimento do projeto.
- **SQLite**: Banco de dados utilizado para armazenar os dados.
- **Python**: Linguagem de programação principal.

## Instalação 

1. Clone o repositório:
   ```bash
   git clone https://github.com/Naiarapacheco/Projeto-faculdade.git

2. Instale as dependências:
    pip install -r requirements.txt

3. Aplique as migrações:
    python manage.py migrate

4. (Opcional) Crie um superusuário para acessar o painel administrativo:
    python manage.py createsuperuser

5. Rode o servidor de desenvolvimento:
    python manage.py runserver
