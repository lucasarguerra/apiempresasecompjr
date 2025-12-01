from fastapi import FastAPI
from schemas.empresas import EmpresaDadosGerais
from config.db import Session 
from model.empresa import Empresa
app = FastAPI()
@app.get("/")
def get_info():
    return {"message": "Hello, World!"}


@app.post("/empresas")
def create_empresa(empresas: EmpresaDadosGerais):
    with Session() as session:
        nova_empresa = Empresa(
        nome=empresas.name,
        cnpj=empresas.cnpj,
        cidade=empresas.cidade,
        ramo_atuacao=empresas.ramo_atuacao,
        telefone=empresas.telefone,
        email_contato=empresas.email
        )
        session.add(nova_empresa)
        session.commit()
        session.refresh(nova_empresa)
    return {
    "name": empresas.name,
    "cnpj": empresas.cnpj,
    "cidade": empresas.cidade,
    "ramo_atuacao": empresas.ramo_atuacao,
    "telefone": empresas.telefone,
    "email": empresas.email

}