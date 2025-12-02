from pydantic import BaseModel
from datetime import date

class EmpresaDadosGerais(BaseModel):
    name: str
    cnpj: str
    cidade:str
    ramo_atuacao:str
    telefone:str
    email:str
    data_de_cadastro: date


class EmpresaDadosAtualizados(BaseModel):
    name:str
    cidade:str
    ramo_atuacao:str
    email:str
    telefone:str