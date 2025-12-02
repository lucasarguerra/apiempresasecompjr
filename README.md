<h1>API de Empresas Clientes</h1>

<p>API desenvolvida com <strong>FastAPI</strong> e <strong>PostgreSQL</strong> para cadastro e gerenciamento de empresas clientes. 
O sistema permite criar, listar, buscar, filtrar, atualizar e excluir empresas, seguindo o padrão REST.</p>

<hr>

<h2>Tecnologias Utilizadas</h2>
<ul>
  <li>Python 3.14</li>
  <li>FastAPI</li>
  <li>SQLAlchemy</li>
  <li>PostgreSQL</li>
  <li>Pydantic</li>
  <li>pytest (para testes automatizados)</li>
</ul>

<hr>

<h2>Como Rodar o Projeto</h2>
<ol>
  <li>Crie e ative o ambiente virtual:
    <pre><code>python -m venv .venv
.venv\Scripts\activate</code></pre>
  </li>

  <li>Instale as dependências:
    <pre><code>pip install -r requirements.txt</code></pre>
  </li>

  <li>Inicie o servidor:
    <pre><code>uvicorn main:app --reload</code></pre>
  </li>

  <li>Acesse a documentação automática:
    <pre><code>http://127.0.0.1:8000/docs</code></pre>
  </li>
</ol>

<hr>

<h2>Estrutura do Projeto</h2>
<pre>
📁 ecompjr-prosel
 ┣ 📂 config
 ┃ ┗ db.py
 ┣ 📂 model
 ┃ ┗ empresa.py
 ┣ 📂 schemas
 ┃ ┗ empresas.py
 ┣ 📄 main.py
 ┣ 📄 test_api_empresas.py
 ┗ 📄 README.md
</pre>

<hr>

<h2>Endpoints da API</h2>

<h3>1. Cadastrar nova empresa</h3>
<p><strong>POST</strong> <code>/empresas</code></p>

<p>Cria um novo registro de empresa no banco.</p>

<p><strong>Exemplo de corpo JSON:</strong></p>
<pre><code>{
  "name": "InfoJr",
  "cnpj": "123456789",
  "cidade": "Feira de Santana",
  "ramo_atuacao": "Tecnologia",
  "telefone": "75999990000",
  "email": "contato@infojr.com",
  "data_de_cadastro": "2025-01-01"
}</code></pre>

<p><strong>Respostas possíveis:</strong></p>
<ul>
  <li>200 OK → Empresa cadastrada com sucesso</li>
  <li>400 Bad Request → CNPJ ou e-mail já cadastrados</li>
</ul>

<hr>

<h3>2. Listar todas as empresas</h3>
<p><strong>GET</strong> <code>/empresas</code></p>

<p>Retorna todas as empresas cadastradas no sistema.</p>

<p><strong>Exemplo de resposta:</strong></p>
<pre><code>[
  {
    "id": 1,
    "name": "InfoJr",
    "cidade": "Feira de Santana",
    "ramo_atuacao": "Tecnologia",
    "telefone": "75999990000",
    "email": "contato@infojr.com",
    "data_de_cadastro": "2025-01-01"
  }
]</code></pre>

<hr>

<h3>3. Buscar empresa pelo nome</h3>
<p><strong>GET</strong> <code>/empresas_buscar?name=Info</code></p>

<p>Permite procurar empresas pelo nome (busca parcial, sem diferenciar maiúsculas/minúsculas).</p>

<p><strong>Respostas possíveis:</strong></p>
<ul>
  <li>200 OK → Retorna lista com as empresas encontradas</li>
  <li>404 Not Found → Nenhuma empresa encontrada</li>
</ul>

<hr>

<h3>4. Filtrar empresas</h3>
<p><strong>GET</strong> <code>/empresas/filtros?cidade=Feira&ramo_atuacao=Tecnologia</code></p>

<p>Filtra as empresas de acordo com cidade e/ou ramo de atuação. Ambos os filtros são opcionais.</p>

<p><strong>Exemplo de resposta:</strong></p>
<pre><code>[
  {
    "id": 1,
    "name": "InfoJr",
    "cidade": "Feira de Santana",
    "ramo_atuacao": "Tecnologia",
    "email": "contato@infojr.com"
  }
]</code></pre>

<hr>

<h3>5. Buscar empresa por ID</h3>
<p><strong>GET</strong> <code>/empresas/{empresa_id}</code></p>

<p>Retorna todos os dados de uma empresa específica.</p>

<p><strong>Exemplo:</strong></p>
<pre><code>GET /empresas/1</code></pre>

<p><strong>Respostas:</strong></p>
<ul>
  <li>200 OK → Empresa encontrada</li>
  <li>404 Not Found → ID não encontrado</li>
</ul>

<hr>

<h3>6. Atualizar empresa</h3>
<p><strong>PUT</strong> <code>/empresas/{empresa_id}</code></p>

<p>Permite editar os dados de uma empresa (exceto CNPJ e data de cadastro).</p>

<p><strong>Exemplo de corpo JSON:</strong></p>
<pre><code>{
  "name": "InfoJr Atualizada",
  "cidade": "Feira de Santana",
  "ramo_atuacao": "Tecnologia",
  "telefone": "75988887777",
  "email": "novoemail@infojr.com"
}</code></pre>

<p><strong>Respostas:</strong></p>
<ul>
  <li>200 OK → Dados atualizados</li>
  <li>404 Not Found → Empresa não encontrada</li>
</ul>

<hr>

<h3>7. Deletar empresa</h3>
<p><strong>DELETE</strong> <code>/empresas/{empresa_id}</code></p>

<p>Remove uma empresa do banco de dados.</p>

<p><strong>Respostas:</strong></p>
<ul>
  <li>200 OK → Empresa deletada com sucesso</li>
  <li>404 Not Found → Empresa não encontrada</li>
</ul>

<hr>

<h3>8. Rota inicial</h3>
<p><strong>GET</strong> <code>/</code></p>

<p>Retorna uma mensagem simples confirmando que a API está ativa.</p>

<p><strong>Exemplo de resposta:</strong></p>
<pre><code>{
  "message": "API de Empresas Clientes - EcompJr"
}</code></pre>

<hr>

<h2>Testes Automatizados</h2>
<p>Os testes foram criados com <strong>pytest</strong> e cobrem as principais rotas (CRUD, filtros e busca). 
O módulo de testes utiliza um banco SQLite isolado para não afetar o banco principal.</p>

<p><strong>Para rodar os testes:</strong></p>
<pre><code>pytest test_api_empresas.py -v</code></pre>
Importante ressaltar que para uma melhor experiência usando os testes, é necessário mexer um pouco no código, já que o de atualização vai falhar no primeiro, pois não existe nenhuma empresa cadastrada previamente.
<hr>

<h2>Comentários no Código</h2>
<p>O código possui comentários objetivos explicando de forma simples o que cada rota faz, 
as verificações realizadas e os principais retornos. 
Os comentários são diretos e ajudam na leitura e manutenção do código, sem exageros.</p>

<hr>

<h2>Autor</h2>
<p><strong>Lucas Guerra de Araújo</strong><br>
Projeto desenvolvido como parte do processo seletivo da <strong>EcompJr – Empresa Júnior de Computação da UEFS.</strong></p>
