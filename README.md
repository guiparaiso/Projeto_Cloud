# Projeto - Computação em Nuvem (KIT-B · 2025.1)

## 👥 Integrantes

- Guilherme Paraiso  
- Nicholas Balkins


## 🧾 Descrição do Projeto

Este projeto implementa uma **API REST** com três funcionalidades principais:

1. **Cadastro de Usuários**  
   - Registra usuários com login e senha.  
   - Gera uma **chave única (token)** por usuário.  
   - Evita cadastros duplicados.

2. **Login de Usuários**  
   - Retorna o **token** do usuário caso as credenciais estejam corretas.  
   - Se inválidas, retorna erro.

3. **Consulta de Cotação (Dólar ↔ Euro)**  
   - Requer um **token válido** para autenticação.  
   - Retorna a cotação atual.  
   - Se o token for inválido, retorna erro.


## 🛠️ Tecnologias Utilizadas

- Python  
- Postgresql  
- Docker  
- Docker Compose

---

## 🧪 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone <https://github.com/guiparaiso/Projeto_Cloud.git>

```

### 2. (Opcional) Crie e ative um ambiente virtual

``` bash

python -m venv venv

#Ativando o ambiente

source .venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
venv\Scripts\Activate.ps1     #Powershell

```

### 3. Instale as dependências
```bash

pip install -r requirements.txt

```

### 4. Criando o seu .env

Um passo **muito** importante é você criar seu  _.env_ dentro de .api

Para lhe ajudar, siga esse modelo:

```bash
POSTGRES_USER= user
POSTGRES_PASSWORD= password
POSTGRES_DB= db
SECRET_KEY= exemplo-123
ALGORITHM= HS256
ALPHA_VANTAGE_API_KEY= sua key Alpha Vantage para a consulta Euro / Dolar funcionar!
```

### 5. Agora sim! Execute com Docker Compose, mas antes ***inicie o Docker no seu computador!!***

```bash
# Entre na pasta do compose.yaml
cd api
#Agora o docker está pronto para rodar!
docker-compose up
```

Acesse a documentação interativa em:
 http://localhost:8080/docs

## Para a documentação completa do projeto, acesse:

👉 Link do MKDocs: https://guiparaiso.github.io/Cloudb/



Link do Docker Hub:  https://hub.docker.com/repository/docker/guiparaiso/fastapi-app/general

Link da API funcionando localmente: https://youtu.be/SqUgc80EK4w

Link Da API funcionando na AWS: https://youtu.be/cRZtIGAxQXA


