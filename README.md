# ibmecjr-mailer
## Descrição
API, para enviar email com dados do formulário para o email do comercial, utilizando o smtplib 
## Tecnologias
FastAPI, pydantic, uvicorn, python-dotenv
## Como rodar localmente 
1. python -m venv venv
2. pip install -r requirements.txt
3. uvicorn main:app --reload
## Variáveis de ambiente
SMTP_USER = email de origem
SMTP_PASS = chave do email de origem
DEST_EMAIL = email de destino 
## Endpoints
- `/contato`: Endpoint principal que envia o email com as informações no POST
- `/health`: Endpoint para checar disponibilidade da API sem precisar disparar emails de teste
