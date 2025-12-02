from pydantic import BaseModel
from datetime import date

# Schema usado no cadastro de novas empresas
class EmpresaDadosGerais(BaseModel):
    name: str
    cnpj: str
    cidade: str
    ramo_atuacao: str
    telefone: str
    email: str
    data_de_cadastro: date


# Schema usado para atualizar os dados de uma empresa já existente
class EmpresaDadosAtualizados(BaseModel):
    name: str
    cidade: str
    ramo_atuacao: str
    email: str
    telefone: str
