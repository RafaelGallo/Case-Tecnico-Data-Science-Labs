import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from scipy.stats import zscore

# Conexão com banco SQLite
engine = create_engine(r"sqlite:///C:/Users/rafae.RAFAEL_NOTEBOOK/Downloads/case_tecnico_paipe/db/tokyo.sqlite")

# Cria pasta do banco se não existir
os.makedirs(r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\db", exist_ok=True)

# Lê as views do banco
train = pd.read_sql("SELECT * FROM vw_train", engine)
test = pd.read_sql("SELECT * FROM vw_test", engine)

# Exibe todas as colunas
pd.set_option('display.max_columns', None)

# Cópia do treino para EDA
df_eda = train.copy()

# Converte colunas numéricas para float
colunas_num = [
    'Area', 'TotalFloorArea', 'Frontage', 'Breadth', 'CoverageRatio',
    'FloorAreaRatio', 'BuildingYear', 'UnitPrice', 'PricePerTsubo',
    'MinTimeToNearestStation', 'MaxTimeToNearestStation', 'TradePrice'
]
for col in colunas_num:
    if col in df_eda.columns:
        df_eda[col] = pd.to_numeric(df_eda[col], errors='coerce')

# Preenche valores ausentes em categorias com 'Unknown'
colunas_cat = [
    'Type', 'Region', 'Prefecture', 'Municipality', 'Structure',
    'LandShape', 'Direction', 'Use', 'Purpose', 'Renovation',
    'Classification', 'FloorPlan'
]
for col in colunas_cat:
    if col in df_eda.columns:
        df_eda[col] = df_eda[col].fillna("Unknown")

# Remove colunas irrelevantes
colunas_para_drop = ['Remarks']
df_eda = df_eda.drop(columns=[col for col in colunas_para_drop if col in df_eda.columns])

# Mostra quantidade de nulos
print(df_eda.isnull().sum())

# Mostra percentual de nulos
print((df_eda.isnull().mean() * 100).sort_values(ascending=False))

# Mostra apenas colunas com pelo menos um nulo
print(df_eda.isnull().sum()[df_eda.isnull().sum() > 0])

# Preenche nulos numéricos com zero
cols_para_zero = [
    'PricePerTsubo', 'UnitPrice', 'TotalFloorArea', 'Frontage', 'Breadth',
    'BuildingYear', 'MaxTimeToNearestStation', 'TimeToNearestStation', 'AgeAtSale',
    'MinTimeToNearestStation', 'CoverageRatio', 'FloorAreaRatio',
    'CityPlanning', 'NearestStation', 'DistrictName'
]
for col in cols_para_zero:
    if col in df_eda.columns:
        df_eda[col] = df_eda[col].fillna(0)

# Preenche categorias restantes com 'Unknown'
categoricas = df_eda.select_dtypes(include=['object']).columns.tolist()
for col in categoricas:
    df_eda[col] = df_eda[col].fillna('Unknown')

# Checa se ainda há nulos
n_nulos_eda = df_eda.isnull().sum().sum()
print(n_nulos_eda)

# Checa duplicatas
n_duplicados = df_eda.duplicated().sum()
print(n_duplicados)
if n_duplicados > 0:
    print(df_eda[df_eda.duplicated()].head())
else:
    print("Não há duplicatas.")

# Função para boxplot e outliers
def analisar_outlier(coluna):
    if coluna in df_eda.columns:
        Q1 = df_eda[coluna].quantile(0.25)
        Q3 = df_eda[coluna].quantile(0.75)
        IQR = Q3 - Q1
        limite_inf = Q1 - 1.5 * IQR
        limite_sup = Q3 + 1.5 * IQR
        outliers = df_eda[(df_eda[coluna] < limite_inf) | (df_eda[coluna] > limite_sup)][coluna]
        print(f"{coluna}: {len(outliers)} outliers encontrados.")
        print("Limite inferior:", limite_inf, "Limite superior:", limite_sup)
        print(outliers.sort_values().head())
        print(outliers.sort_values(ascending=False).head())
        plt.figure(figsize=(8, 1.5))
        sns.boxplot(x=df_eda[coluna], color="skyblue", fliersize=2)
        plt.title(f"Boxplot de {coluna}")
        plt.show()
    else:
        print(f"Coluna {coluna} não encontrada.")

# Remove outliers pelo Z-score
colunas_outlier = ['Area', 'TradePrice']
z_scores = df_eda[colunas_outlier].apply(zscore)
limite_z = 3
mascara = (np.abs(z_scores) < limite_z).all(axis=1)
df_eda = df_eda[mascara]

# Exporta os dados limpos
pasta_destino = r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\input"
os.makedirs(pasta_destino, exist_ok=True)
csv_path = os.path.join(pasta_destino, "df_eda_limpo.csv")
excel_path = os.path.join(pasta_destino, "df_eda_limpo.xlsx")
df_eda.to_csv(csv_path, index=False, encoding="utf-8-sig")
df_eda.to_excel(excel_path, index=False, engine="openpyxl")
print(csv_path)
print(excel_path)