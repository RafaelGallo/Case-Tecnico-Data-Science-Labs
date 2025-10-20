# Importação das bibliotecas necessárias
import pandas as pd
import os
from sqlalchemy import create_engine
from tqdm import tqdm


def get_engine(db_path="db/tokyo.sqlite"):
    """
    Cria e retorna uma conexão (engine) com o banco SQLite.
    Caso o diretório informado não exista, ele será criado automaticamente.
    """
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    engine = create_engine(f"sqlite:///{db_path}", future=True)
    return engine


def standardize_columns(df):
    """
    Padroniza os nomes das colunas que contêm quebras de linha (\n)
    para garantir compatibilidade no momento da importação.
    """
    return df.rename(columns={
        "TimeToNearestSt\nation": "TimeToNearestStation",
        "MinTimeToNeare\nstStation": "MinTimeToNearestStation",
        "MaxTimeToNeare\nstStation": "MaxTimeToNearestStation",
        "AreaIsGreaterFla\ng": "AreaIsGreaterFlag",
        "FrontageIsGreate\nrFlag": "FrontageIsGreaterFlag",
        "TotalFloorAreaIs\nGreater": "TotalFloorAreaIsGreater"
    })


def load_csv_to_sqlite(csv_path, engine, table_name="transactions",
                       if_exists="append", chunksize=10000):
    """
    Lê um arquivo CSV e o carrega em uma tabela SQLite.
    O carregamento é feito em blocos (chunks) para otimizar o uso de memória.
    """
    # Conta o número total de linhas do arquivo (exceto o cabeçalho)
    total = sum(1 for _ in open(csv_path, encoding="utf-8")) - 1
    reader = pd.read_csv(csv_path, chunksize=chunksize)
    first_chunk = True if if_exists == "replace" else False

    # Loop de leitura e inserção dos dados no banco com barra de progresso
    with tqdm(total=total, desc=f"Importando {os.path.basename(csv_path)}") as pbar:
        for chunk in reader:
            # Padroniza os nomes das colunas
            chunk = standardize_columns(chunk)

            # Insere os dados na tabela SQLite
            chunk.to_sql(
                table_name,
                con=engine,
                if_exists="replace" if first_chunk else "append",
                index=False,
            )

            # Atualiza o controle de primeira inserção e a barra de progresso
            first_chunk = False
            pbar.update(len(chunk))

    # Mensagem final de confirmação
    print(f"{csv_path} importado para tabela '{table_name}' ({total} linhas).")


if __name__ == "__main__":
    # Cria a conexão com o banco
    engine = get_engine()

    # Importa o conjunto de treino e substitui a tabela se já existir
    load_csv_to_sqlite(
        r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\data\train_houses.csv",
        engine, if_exists="replace"
    )

    # Importa o conjunto de teste (sem a variável alvo)
    load_csv_to_sqlite(
        r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\data\test_houses.csv",
        engine, if_exists="append"
    )

    # Confirmação final de criação e carga do banco
    print("Banco de dados criado e populado com sucesso.")