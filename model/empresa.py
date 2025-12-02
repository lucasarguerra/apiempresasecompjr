from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from config.db import engine

Base = declarative_base()

# Modelo que representa a tabela de empresas no banco de dados
class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)  # Identificador único
    name = Column(String(150), nullable=False)  # Nome da empresa
    cnpj = Column(String(18), unique=True, nullable=False, index=True)  # CNPJ, deve ser único
    cidade = Column(String(100), nullable=False)  # Cidade onde a empresa está localizada
    ramo_atuacao = Column(String(100), nullable=False)  # Área de atuação da empresa
    telefone = Column(String(20), nullable=True)  # Telefone de contato (opcional)
    email = Column(String(120), unique=True, nullable=False, index=True)  # E-mail, também único
    data_de_cadastro = Column(Date)  # Data em que a empresa foi cadastrada

# Cria a tabela no banco caso ainda não exista
Base.metadata.create_all(engine)
