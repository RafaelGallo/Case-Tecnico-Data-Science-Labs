# src/etl.py
import pandas as pd
from sqlalchemy import text
from tqdm import tqdm

def _standardize_cols(df):
    # padroniza nomes idênticos aos do schema (evita conflito)
    return df.rename(columns={
        "TimeToNearestSt\nation": "TimeToNearestStation",   # se vier quebrado
        "MinTimeToNeare\nstStation": "MinTimeToNearestStation",
        "MaxTimeToNeare\nstStation": "MaxTimeToNearestStation",
        "AreaIsGreaterFla\ng": "AreaIsGreaterFlag",
        "FrontageIsGreate\nrFlag": "FrontageIsGreaterFlag",
        "TotalFloorAreaIs\nGreater": "TotalFloorAreaIsGreater"
    })

def load_csv_to_sql(engine, csv_path, table_name="transactions", if_exists="replace"):
    df = pd.read_csv(csv_path)
    df = _standardize_cols(df)
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)

def split_train_test_in_db(engine):
    # Mantém uma única tabela e cria VIEWS para train/test
    with engine.begin() as conn:
        # Assume que dados de teste não têm TradePrice (nulos)
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

# scripts rápidos (executar no terminal ou em célula do notebook)
from src.db_utils import get_engine
from src.etl import load_csv_to_sql, split_train_test_in_db

engine = get_engine()
load_csv_to_sql(engine, "data/raw/train.csv", if_exists="replace")
# append o test (mesmas colunas, sem TradePrice)
load_csv_to_sql(engine, "data/raw/test.csv", if_exists="append")
split_train_test_in_db(engine)
print("✅ Train/Test disponíveis como views vw_train e vw_test.")
