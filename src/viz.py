# Importação de bibliotecas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_pred_scatter(y_true, y_pred, path=None):
    """
    Gera um gráfico de dispersão entre os valores reais e previstos.
    Mostra a linha de referência (y = x) para indicar o ajuste ideal.
    """
    plt.figure(figsize=(6, 6))
    sns.scatterplot(x=y_true, y=y_pred, alpha=0.3)
    lim = [0, max(np.max(y_true), np.max(y_pred)) * 1.05]
    plt.plot(lim, lim, ls="--")
    plt.xlabel("Real")
    plt.ylabel("Previsto")
    plt.title("Real vs Previsto")
    if path:
        plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_residuals(y_true, y_pred, path=None):
    """
    Plota a distribuição dos resíduos (diferença entre o valor previsto e o real).
    Permite avaliar o padrão dos erros e possíveis vieses no modelo.
    """
    res = y_pred - y_true
    plt.figure(figsize=(6, 4))
    sns.histplot(res, kde=True)
    plt.title("Distribuição dos resíduos")
    if path:
        plt.savefig(path, dpi=160, bbox_inches="tight")


def plot_mape_bins(y_true, y_pred, bins=10, path=None):
    """
    Calcula e exibe o MAPE médio (erro percentual absoluto) em diferentes
    faixas de preço. As faixas são definidas por quantis do valor real.
    """
    df = pd.DataFrame({"y": y_true, "p": y_pred})
    df["bin"] = pd.qcut(df["y"], q=bins, duplicates="drop")
    mape_by_bin = df.groupby("bin").apply(
        lambda d: np.mean(np.abs((d["y"] - d["p"]) / (d["y"] + 1e-7))) * 100
    )
    mape_by_bin.plot(kind="bar", figsize=(8, 4), rot=45, title="MAPE por faixas de preço")
    if path:
        plt.savefig(path, dpi=160, bbox_inches="tight")


# Importa as funções de visualização
from src.viz import plot_pred_scatter, plot_residuals, plot_mape_bins

# Gera gráficos de validação
plot_pred_scatter(yva.values, pred_val, "outputs/figs/val_scatter.png")
plot_residuals(yva.values, pred_val, "outputs/figs/val_residuals.png")
plot_mape_bins(yva.values, pred_val, bins=8, path="outputs/figs/val_mape_bins.png")

# Exibe a importância das variáveis
fi = final_model.get_feature_importance(prettified=True)
fi.sort_values("Importances", ascending=False).head(20)

# Treinamento final do modelo com todos os dados de treino
full_model = CatBoostRegressor(
    loss_function="RMSE",
    learning_rate=0.05,
    depth=8,
    l2_leaf_reg=6.0,
    iterations=8000,
    random_seed=42,
    eval_metric="RMSE",
    early_stopping_rounds=300,
    verbose=200,
)

# Treina o modelo completo com conjunto de treino
full_model.fit(
    Pool(
        train[use_cols],
        train[TARGET],
        cat_features=[
            train[use_cols].columns.get_loc(c)
            for c in cat_cols
            if c in use_cols
        ],
    ),
    eval_set=Pool(
        train[use_cols].iloc[:2000],
        train[TARGET].iloc[:2000],
        cat_features=[
            train[use_cols].columns.get_loc(c)
            for c in cat_cols
            if c in use_cols
        ],
    ),
)

# Gera previsões no conjunto de teste
test_pred = full_model.predict(test[use_cols])

# Cria DataFrame de submissão
sub = test[["No"]].copy()
sub["TradePrice"] = np.clip(test_pred, a_min=0, a_max=None).astype(float)

# Salva o CSV de submissão
sub_path = "outputs/submissions/predictions.csv"
sub.to_csv(sub_path, index=False)
print("CSV gerado:", sub_path, sub.head())
