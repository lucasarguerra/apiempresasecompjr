from fastapi import FastAPI
from schemas.empresas import EmpresaDadosGerais
app = FastAPI()
@app.get("/")
def get_info():
    return {"message": "Hello, World!"}


@app.post("/")
def create_empresa(empresas: EmpresaDadosGerais):
    return {
    "name": empresas.name,
    "cnpj": empresas.cnpj,
    "cidade": empresas.cidade,
    "ramo_atuacao": empresas.ramo_atuacao,
    "telefone": empresas.telefone,

}