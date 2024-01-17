# Utilizando FastAPI para criar uma API

from fastapi import FastAPI
app = FastAPI()

# Criando uma rota
@app.get("/api/hello") #Endpoint = rota/nome da rota
def helloWorld():
    return {"mensagem": "Hello World!"}

# Criando uma rota com parâmetro
@app.get("/api/hello/{nome}")
def helloWorld_(nome: str):
    return {"mensagem": f"Hello {nome}!"}

# Criando uma rota com parâmetro opcional
@app.get("/api/hello/{nome}") 
def helloWorld__(nome: str, sobrenome: str = None): #type:ignore
    if sobrenome:
        return {"mensagem": f"Hello {nome} {sobrenome}!"}
    return {"mensagem": f"Hello {nome}!"}

# Para executar o servidor, digite no terminal:
# uvicorn nome_do_arquivo:nome_do_app --reload
