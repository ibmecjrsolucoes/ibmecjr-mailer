from fastapi import FastAPI

app = FastAPI()










@app.post("/contato")
def receber_email():
    
    return {"message":"Formulário enviado com sucesso!"}