from pydantic import BaseModel


class EmpresaDadosGerais(BaseModel):
    name: str
    cnpj: str
    cidade:str
    ramo_atuacao:str
    telefone:str
    email:str

class EmpresaDadosAtualizados(BaseModel):
    name:str
    cidade:str
    modo_atuacao:str
    email:str
    tel:str