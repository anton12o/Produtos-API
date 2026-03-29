                                    Produtos API
API REST desenvolvida como projeto prático de estudo, utilizando Python, FastAPI e PostgreSQL.

Tecnologias utilizadas:

- Python com FastAPI — criação dos endpoints e regras da aplicação
- SQLModel — mapeamento das tabelas e interação com o banco de dados
- PostgreSQL — banco de dados relacional
- Docker + Docker Compose — containerização da aplicação e do banco
- Railway — deploy em produção

Funcionalidades do projeto:

  Método:          Rota:              Descrição:

- GET             /health             Verifica se a API está ativa
- POST           /produtos/           Cadastra um novo produto
- GET            /produtos/           Lista todos os produtos
- GET            /produtos/{id}       Busca um produto por ID
- DELETE         /produtos/{id}       Remove um produto


Estrutura do projeto:

- main.py: corpo da aplicação, classes e endpoints
- .env: variáveis de ambiente para proteger dados sensíveis como senha do banco
- docker-compose.yml: configuração dos serviços (API e banco de dados)
- Dockerfile: instruções de build e inicialização da aplicação
- requirements.txt: dependências utilizadas pela aplicação

Como executar localmente:

-No terminal coloque: 

docker-compose up --build

Acesse a documentação para ver o estado da mesma em: `http://localhost:8000/docs`

Com a API ja disponivel, acesse os documentos e teste-a aqui:

https://produtos-api-production-4930.up.railway.app/docs
