# Projeto - Computação em Nuvem (KIT-B · 2025.1)
---

:Integrantes
Guilherme Paraiso

Nicholas Balkins

---



🧾 Descrição do Projeto
Este projeto implementa uma API REST com três funcionalidades principais:

Cadastro de Usuários

Registra usuários com login e senha.

Gera uma chave única (token) por usuário.

Evita cadastros duplicados.

Login de Usuários

Retorna o token do usuário caso as credenciais estejam corretas.

Se inválidas, retorna erro.

Consulta de Cotação (Dólar ↔ Euro)

Requer um token válido para autenticação.

Retorna a cotação atual.

Se o token for inválido, retorna erro.

🛠️ Tecnologias Utilizadas
Python

FastAPI

SQLite

Docker

Docker Compose

🧪 Como Executar o Projeto
1. Clone o repositório esse repositório

cd <api>

2. (Opcional) Ambiente Virtual
bash
Copy
Edit
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows


3. Instale as dependências
bash
Copy
Edit
pip install -r requirements.txt


4. Execute com Docker Compose


bash
Copy
Edit
docker-compose up


Acesse a documentação interativa em:
👉 http://localhost:8000/docs


Link do MKDocs: https://guiparaiso.github.io/Cloudb/

Link do Docker Hub:  https://hub.docker.com/repository/docker/guiparaiso/fastapi-app/general

Local do Compose Yaml: /api
