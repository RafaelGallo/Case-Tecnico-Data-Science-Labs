"""
main.py

Pipeline ETL para o projeto Tokyo Real Estate.
Executa a carga dos arquivos CSV de treino e teste para o banco SQLite,
com barra de progresso (tqdm) implementada no ETL.
Após a carga, cria views SQL para separar treino e teste.

Autor: Rafael Gallo
Data: 2025-10-18
"""

import argparse
from src.etl import get_engine, load_csv_to_sqlite
from sqlalchemy import text

def create_views(engine):
    """
    Cria as views vw_train e vw_test no banco SQLite.

    Parâmetros
    ----------
    engine : sqlalchemy.Engine
        Instância da conexão com o banco de dados SQLite.
    """
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

def main(args):
    """
    Executa o pipeline de ETL: carrega arquivos CSV no banco SQLite e cria views.

    Parâmetros
    ----------
    args : argparse.Namespace
        Argumentos de linha de comando com caminhos dos arquivos.
    """
    # Cria engine de conexão com o banco SQLite
    engine = get_engine(args.db_path)

    # Importa o arquivo CSV de treino para o banco com barra de progresso (tqdm)
    # A barra de progresso é exibida durante a carga, implementada na função load_csv_to_sqlite.
    load_csv_to_sqlite(
        args.train_csv,
        engine,
        if_exists="replace"
    )

    # Importa o arquivo CSV de teste para o banco com barra de progresso (tqdm)
    load_csv_to_sqlite(
        args.test_csv,
        engine,
        if_exists="append"
    )

    print("Banco de dados criado e populado.")

    # Cria as views para treino e teste
    create_views(engine)

if __name__ == "__main__":
    # Parser de argumentos de linha de comando
    parser = argparse.ArgumentParser(description="Pipeline ETL Tokyo Real Estate")
    parser.add_argument(
        "--db_path",
        type=str,
        default="db/tokyo.sqlite",
        help="Caminho do arquivo SQLite."
    )
    parser.add_argument(
        "--train_csv",
        type=str,
        required=True,
        help=r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\data\train_houses.csv"
    )
    parser.add_argument(
        "--test_csv",
        type=str,
        required=True,
        help=r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\data\test_houses.csv"
    )
    args = parser.parse_args()

    # Executa o pipeline principal
    main(args)