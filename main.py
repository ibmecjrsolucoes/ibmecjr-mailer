from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://127.0.0.1:8000"],
    allow_methods = ["POST", "OPTIONS"],
    allow_headers = ["Content-Type"],
)

class ContatoForm(BaseModel):
    nome: str
    email: str
    empresa: str
    cargo: str
    funcionarios: str
    segmento: str
    servico: List[str]
    servicoOutro: Optional[str] = ""
    desafioPrincipal: str
    prazoSolucao: str
    resultadoEsperado: str


def enviar_email(form: ContatoForm):
    smtp_user  = os.getenv("SMTP_USER")
    smtp_pass  = os.getenv("SMTP_PASS")
    dest_email = os.getenv("DEST_EMAIL")

    msg = MIMEMultipart()
    msg["Subject"] = f"Novo Lead: {form.nome} — {form.empresa}"
    msg["From"]    = smtp_user
    msg["To"]      = dest_email
    msg["Reply-To"] = form.email

    corpo = f"""
    Nome: {form.nome}
    Email: {form.email}
    Empresa: {form.empresa}
    Cargo: {form.cargo}
    Funcionários: {form.funcionarios}
    Segmento: {form.segmento}
    Serviços: {", ".join(form.servico)}
    Desafio: {form.desafioPrincipal}
    Prazo: {form.prazoSolucao}
    Resultado esperado: {form.resultadoEsperado}
    """

    msg.attach(MIMEText(corpo, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(smtp_user, dest_email, msg.as_string())




@app.post("/contato")
def receber_email(form: ContatoForm):
    enviar_email(form)
    return {"message":"Formulário enviado com sucesso!"}