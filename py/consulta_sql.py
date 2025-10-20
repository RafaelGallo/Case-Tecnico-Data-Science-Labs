# Importação das bibliotecas
import pandas as pd
import os
from sqlalchemy import create_engine, text

# Garante que o diretório do banco existe
os.makedirs(r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\db", exist_ok=True)

# Cria conexão com o banco SQLite
engine = create_engine(
    r"sqlite:///C:/Users/rafae.RAFAEL_NOTEBOOK/Downloads/case_tecnico_paipe/db/tokyo.sqlite"
)

# Criação das views de treino e teste
with engine.begin() as conn:
    conn.execute(text("DROP VIEW IF EXISTS vw_train"))
    conn.execute(text("DROP VIEW IF EXISTS vw_test"))
    conn.execute(text("""
        CREATE VIEW vw_train AS
        SELECT * FROM transactions WHERE TradePrice IS NOT NULL
    """))
    conn.execute(text("""
        CREATE VIEW vw_test AS
        SELECT * FROM transactions WHERE TradePrice IS NULL
    """))

print("Views criadas: vw_train (treino) e vw_test (teste)")

# Leitura das views
train = pd.read_sql("SELECT * FROM vw_train", engine)
test = pd.read_sql("SELECT * FROM vw_test", engine)

# Consulta simples: contagem e preço médio de imóveis com área > 100 m²
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT COUNT(*) AS n, AVG(TradePrice) AS avg_price
        FROM vw_train
        WHERE Area > 100
    """))
    row = result.fetchone()
    print("Quantidade de imóveis área > 100m²:", row.n)
    print("Preço médio:", row.avg_price)

# Consulta filtrando por município
municipality = "Adachi Ward"
df = pd.read_sql(
    text("SELECT * FROM vw_train WHERE Municipality = :muni"),
    engine,
    params={"muni": municipality}
)
df.head()

# Lista todas as tabelas e views no banco
df_views = pd.read_sql(
    "SELECT name, type FROM sqlite_master WHERE type IN ('table','view')", engine
)
df_views

# Estatísticas por região: contagem, média e preço máximo
df_stats = pd.read_sql("""
    SELECT Region, COUNT(*) AS n, AVG(TradePrice) AS avg_price, MAX(TradePrice) AS max_price
    FROM vw_train
    GROUP BY Region
    ORDER BY avg_price DESC
""", engine)
df_stats

# Função auxiliar para carregar instruções SQL externas
def read_sql_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Executa script SQL externo (sem parâmetros)
sql_query = read_sql_file(r"../sql/select_top10_residenciais.sql")
df = pd.read_sql(sql_query, engine)
df

# Executa script SQL externo (com parâmetros)
sql_query = read_sql_file(r"../sql/top_adachi_ward.sql")
df = pd.read_sql(text(sql_query), engine, params={"muni": "Adachi Ward"})
df.head()

# Recria engine (boa prática para novos contextos)
engine = create_engine(
    r"sqlite:///C:/Users/rafae.RAFAEL_NOTEBOOK/Downloads/case_tecnico_paipe/db/tokyo.sqlite"
)

# Reutiliza a função de leitura SQL
def read_sql_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Executa SQL externo sem parâmetro
sql_top10 = read_sql_file(r"../sql/select_top10_residenciais.sql")
df_top10 = pd.read_sql(sql_top10, engine)
df_top10

# Executa SQL externo com parâmetro (municipalidade)
sql_muni = read_sql_file("../sql/top_adachi_ward.sql")
df_muni = pd.read_sql(text(sql_muni), engine, params={"muni": "Adachi Ward"})
df_muni
