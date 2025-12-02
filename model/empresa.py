from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.orm import declarative_base
from config.db import engine

Base = declarative_base()

class Empresa(Base):
    __tablename__ = 'empresas'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(150), nullable=False)
    cnpj = Column(String(18), unique=True, nullable=False, index=True)
    cidade = Column(String(100), nullable=False)
    ramo_atuacao = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    data_de_cadastro = Column(Date)

# Create the table in the database
Base.metadata.create_all(engine)

