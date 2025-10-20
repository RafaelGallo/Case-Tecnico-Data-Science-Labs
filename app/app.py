# Importação de bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Carregamento do modelo salvo
MODEL_PATH = r"C:\Users\rafae.RAFAEL_NOTEBOOK\Downloads\case_tecnico_paipe\models\GradientBoosting.pkl"
model = joblib.load(MODEL_PATH)

# Definição das features utilizadas no treinamento
FEATURES = [
    'Area', 'TotalFloorArea', 'Frontage', 'Breadth',
    'MaxTimeToNearestStation', 'MinTimeToNearestStation',
    'PricePerTsubo', 'UnitPrice',
    'Type_le', 'Region_le', 'Prefecture_le', 'CityPlanning_le'
    # Adicione outras features do modelo de treino, se necessário
]

# Interface principal
st.title("Predição de Preço de Imóveis — Regressão Linear")

# Entrada manual de dados
st.header("Entrada Manual")
user_input = {}

# Campos de entrada conforme as features
for col in FEATURES:
    if col.endswith('_le') or col in ['MaxTimeToNearestStation', 'MinTimeToNearestStation']:
        user_input[col] = st.number_input(f"{col}", min_value=0, value=0)
    else:
        user_input[col] = st.number_input(f"{col}", value=0.0)

# Botão para previsão manual
if st.button("Prever (entrada manual)"):
    df_input = pd.DataFrame([user_input], columns=FEATURES)
    pred = model.predict(df_input)
    st.success(f"Preço previsto: ¥ {pred[0]:,.0f}")

st.markdown("---")

# Upload e predição em lote
st.header("Upload em Lote (CSV)")
csv_file = st.file_uploader("Envie um arquivo CSV com as colunas exatas usadas no treino", type=['csv'])

if csv_file is not None:
    df_csv = pd.read_csv(csv_file)

    # Garante que todas as colunas necessárias existam e estejam na ordem correta
    for col in FEATURES:
        if col not in df_csv.columns:
            df_csv[col] = 0
    df_csv = df_csv[FEATURES]

    preds = model.predict(df_csv)
    df_csv["Predicted_TradePrice"] = preds

    st.success(f"Previsões geradas para {len(df_csv)} imóveis.")
    st.dataframe(df_csv.head(10))

    # Gera arquivo para download
    csv_result = df_csv.to_csv(index=False).encode()
    st.download_button(
        "Baixar resultado CSV",
        data=csv_result,
        file_name="predicoes_imoveis.csv",
        mime="text/csv"
    )

# Exibe a lista de features esperadas
st.info("Garanta que as features de entrada tenham nomes e ordem idênticos aos usados no treino.")
if st.button("Ver features esperadas"):
    st.code(FEATURES)
