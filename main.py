from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional


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








@app.post("/contato")
def receber_email():
    
    return {"message":"Formulário enviado com sucesso!"}