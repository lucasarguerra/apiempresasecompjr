
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Query
from schemas.empresas import EmpresaDadosGerais, EmpresaDadosAtualizados
from config.db import Session 
from model.empresa import Empresa
app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


#Função para criar uma nova empresa
@app.post("/empresas")
def criar_empresa(empresa: EmpresaDadosGerais, db: Session = Depends(get_db)):
    if db.query(Empresa).filter(Empresa.cnpj == empresa.cnpj).first():
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    
    if db.query(Empresa).filter(Empresa.email == empresa.email).first():
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    db_empresa = Empresa(
        name=empresa.name,
        cnpj=empresa.cnpj,
        cidade=empresa.cidade,
        ramo_atuacao=empresa.ramo_atuacao,
        telefone=empresa.telefone,
        email=empresa.email,
        data_de_cadastro=empresa.data_de_cadastro
    ) 
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa



#Listar todas as empresas
@app.get("/empresas")
def get_empresas(db: Session = Depends(get_db)):
    empresas = db.query(Empresa).all()
    return empresas


@app.get("/empresas/filtros")
def get_empresas_filtros(cidade: Optional[str] = Query(None),
    ramo_atuacao: Optional[str] = Query(None),
    db: Session = Depends(get_db)):
    query = db.query(Empresa)
    if cidade:
        query = query.filter(Empresa.cidade.ilike(f"%{cidade}%"))
    if ramo_atuacao:
        query = query.filter(Empresa.ramo_atuacao.ilike(f"%{ramo_atuacao}%"))
    resultados = query.all()
    if not resultados:
        raise HTTPException(status_code=404, detail="Nenhuma empresa encontrada com os filtros fornecidos")
    return resultados



@app.get("/empresas_buscar")
def buscar_empresas(name: Optional[str] = Query(None),
    db: Session = Depends(get_db)):
    if(not name):
        raise HTTPException(status_code=404, detail="Parâmetros de busca inválidos")
    resultados = db.query(Empresa).filter(Empresa.name.ilike(f"%{name}%")).all()
    if not resultados:
        raise HTTPException(status_code=404, detail="Nenhuma empresa encontrada")
    return resultados

#Procurar empresa por ID
@app.get("/empresas/{empresa_id}")
def get_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if(not db_empresa):
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa



#Função para atualizar uma empresa
@app.put("/empresas/{empresa_id}")
def atualizar_empresa(empresa_id: int, empresa_data: EmpresaDadosAtualizados, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if(not db_empresa):
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    for (key,value) in empresa_data.dict().items():
        setattr(db_empresa, key, value)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa



#Função para deletar uma empresa
@app.delete("/empresas/{empresa_id}")
def deletar_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = db.query(Empresa).filter(Empresa.id == empresa_id).first()
    if(not db_empresa):
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    
    db.delete(db_empresa)
    db.commit()
    return {"detail": "Empresa deletada com sucesso"}



