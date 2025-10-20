# Importação de bibliotecas
import numpy as np
import pandas as pd
import re


def parse_time_window(txt):
    """
    Extrai os valores numéricos de um campo de texto que representa
    um intervalo de tempo até a estação.

    Exemplos:
        "10-15min" → (10, 15, 12.5)
        "10min" → (10, 10, 10)

    Retorna uma tupla com:
        (tempo mínimo, tempo máximo, média)
    """
    if pd.isna(txt):
        return np.nan, np.nan, np.nan

    # Tenta capturar intervalo do tipo "10-15"
    m = re.search(r"(\d+)\s*-\s*(\d+)", str(txt))
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return a, b, (a + b) / 2

    # Captura apenas um valor, caso não haja intervalo
    m2 = re.search(r"(\d+)", str(txt))
    if m2:
        x = int(m2.group(1))
        return x, x, x

    return np.nan, np.nan, np.nan


def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza o pré-processamento básico dos dados de imóveis.

    - Extrai tempos mínimos, máximos e médios até a estação mais próxima.
    - Calcula a idade do imóvel na data da venda.
    - Cria colunas logarítmicas de área.
    - Gera índices de aproveitamento do solo.
    - Cria variáveis binárias para reforma e via privada.
    - Simplifica a direção da fachada (N, S, E, W).

    Retorna um DataFrame limpo e enriquecido.
    """
    df = df.copy()

    # Cria colunas de tempo até a estação (caso não existam)
    if "MinTimeToNearestStation" not in df or "MaxTimeToNearestStation" not in df:
        mins, maxs, means = [], [], []
        for t in df.get("TimeToNearestStation", []):
            a, b, c = parse_time_window(t)
            mins.append(a)
            maxs.append(b)
            means.append(c)

        df["MinTimeToNearestStation"] = df.get("MinTimeToNearestStation", pd.Series(mins))
        df["MaxTimeToNearestStation"] = df.get("MaxTimeToNearestStation", pd.Series(maxs))
        df["MeanTimeToStation"] = df.get("MeanTimeToStation", pd.Series(means))
    else:
        df["MeanTimeToStation"] = (
            df["MinTimeToNearestStation"] + df["MaxTimeToNearestStation"]
        ) / 2

    # Calcula idade do imóvel (ano da transação - ano de construção)
    df["AgeAtSale"] = np.where(
        df["BuildingYear"].notna(), df["Year"] - df["BuildingYear"], np.nan
    )

    # Substitui idades negativas por NaN
    df.loc[df["AgeAtSale"] < 0, "AgeAtSale"] = np.nan

    # Cria colunas logarítmicas para normalização de escala
    if "Area" in df:
        df["LogArea"] = np.log1p(df["Area"].clip(lower=0))
    if "TotalFloorArea" in df:
        df["LogTotalFloorArea"] = np.log1p(df["TotalFloorArea"].clip(lower=0))

    # Cria índice de aproveitamento do solo (FAR / Coverage)
    df["FAR_to_Coverage"] = df["FloorAreaRatio"] / np.clip(
        df["CoverageRatio"].replace(0, np.nan), 1, None
    )

    # Cria variável binária indicando presença de via privada
    df["HasPrivateRoad"] = (
        df.get("Remarks", "")
        .fillna("")
        .str.contains("private road", case=False)
        .astype(int)
    )

    # Cria variável binária indicando se o imóvel foi reformado
    df["IsRenovated"] = (
        df.get("Renovation", "")
        .fillna("")
        .str.contains("yes|done", case=False)
        .astype(int)
    )

    # Simplifica direção da fachada (N/E/S/W)
    df["DirSimple"] = (
        df.get("Direction", "")
        .fillna("")
        .str[0]
        .str.upper()
        .map({"N": "N", "S": "S", "E": "E", "W": "W"})
        .fillna("O")
    )

    return df