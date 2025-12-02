import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db
from model.empresa import Base, Empresa

# ----------------------------------------
# 🔹 CONFIGURAÇÃO DE BANCO DE TESTE ISOLADO
# ----------------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas do modelo no banco de teste
Base.metadata.create_all(bind=engine)

# Substitui a dependência de banco pelo banco de teste
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# ----------------------------------------
# 🔹 FIXTURE: LIMPA O BANCO ANTES DE CADA TESTE
# ----------------------------------------
@pytest.fixture(autouse=True)
def limpar_banco():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield


# ----------------------------------------
# 🔹 TESTES
# ----------------------------------------

def test_criar_empresa():
    """
    Testa cadastro de uma nova empresa.
    """
    data = {
        "name": "InfoJr",
        "cnpj": "123456",
        "cidade": "Feira de Santana",
        "ramo_atuacao": "Tecnologia",
        "telefone": "75999990000",
        "email": "contato@infojr.com",
        "data_de_cadastro": "2025-01-01"
    }
    response = client.post("/empresas", json=data)
    assert response.status_code == 200
    result = response.json()
    assert result["name"] == "InfoJr"
    assert result["cnpj"] == "123456"


def test_listar_empresas():
    """
    Testa listagem de empresas cadastradas.
    """
    # Cadastra uma empresa
    test_criar_empresa()
    response = client.get("/empresas")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_buscar_empresa_por_nome():
    """
    Testa a rota de busca textual /empresas_buscar.
    """
    test_criar_empresa()
    response = client.get("/empresas_buscar?name=Info")
    assert response.status_code == 200
    data = response.json()
    assert any("InfoJr" in empresa["name"] for empresa in data)


def test_filtrar_por_cidade():
    """
    Testa o filtro /empresas/filtros?cidade=Feira
    """
    test_criar_empresa()
    response = client.get("/empresas/filtros?cidade=Feira")
    assert response.status_code == 200
    data = response.json()
    assert all("Feira" in empresa["cidade"] for empresa in data)


def test_atualizar_empresa():
    """
    Testa atualização de dados de uma empresa existente.
    """
    # Cria uma empresa e pega o ID
    response = client.post("/empresas", json={
        "name": "InfoJr",
        "cnpj": "654321",
        "cidade": "Feira de Santana",
        "ramo_atuacao": "TI",
        "telefone": "75999999999",
        "email": "infojr@teste.com",
        "data_de_cadastro": "2025-01-01"
    })
    empresa_id = response.json()["id"]

    # Atualiza alguns campos
    update_data = {
        "name": "InfoJr Atualizada",
        "telefone": "75988887777",
        "email": "novo@infojr.com"
    }
    response = client.put(f"/empresas/{empresa_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["name"] == "InfoJr Atualizada"


def test_deletar_empresa():
    """
    Testa exclusão de uma empresa existente.
    """
    # Cria uma empresa e pega o ID
    response = client.post("/empresas", json={
        "name": "DeleteMe",
        "cnpj": "777777",
        "cidade": "Salvador",
        "ramo_atuacao": "Comércio",
        "telefone": "71999990000",
        "email": "delete@teste.com",
        "data_de_cadastro": "2025-01-01"
    })
    empresa_id = response.json()["id"]

    # Deleta
    response = client.delete(f"/empresas/{empresa_id}")
    assert response.status_code == 200
    assert "deletada" in response.text

    # Confirma exclusão
    response = client.get(f"/empresas/{empresa_id}")
    assert response.status_code == 404
