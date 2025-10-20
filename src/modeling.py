# src/modeling.py
from catboost import CatBoostRegressor, Pool
from src.metrics import rmsle, mape
from sklearn.model_selection import GroupKFold
import numpy as np

def train_catboost_cv(df, target, features, cat_cols, groups, params=None, n_splits=5, seed=42):
    X = df[features]
    y = df[target].values
    gkf = GroupKFold(n_splits=n_splits)
    oof = np.zeros(len(df))
    models = []

    if params is None:
        params = dict(
            loss_function="RMSE",    # otimiza RMSE; RMSLE será métrica externa
            learning_rate=0.05,
            depth=8,
            l2_leaf_reg=6.0,
            iterations=5000,
            random_seed=seed,
            eval_metric="RMSE",
            early_stopping_rounds=200,
            verbose=False
        )

    for tr, va in gkf.split(X, y, groups=groups):
        dtr = Pool(
            data=X.iloc[tr],
            label=y[tr],
            cat_features=[X.columns.get_loc(c) for c in cat_cols if c in X.columns]
        )
        dva = Pool(
            data=X.iloc[va],
            label=y[va],
            cat_features=[X.columns.get_loc(c) for c in cat_cols if c in X.columns]
        )
        model = CatBoostRegressor(**params)
        model.fit(dtr, eval_set=dva, verbose=200)
        pred = model.predict(X.iloc[va])
        oof[va] = pred
        models.append(model)

    return models, oof

from src.modeling import train_catboost_cv
from src.metrics import rmsle, mape

models, oof = train_catboost_cv(train, TARGET, use_cols, cat_cols, groups, n_splits=5)
print("CV RMSLE:", rmsle(train[TARGET], oof))
print("CV MAPE:", mape(train[TARGET], oof))

train_mask = train["Year"] < 2019
val_mask   = train["Year"] == 2019

Xtr, ytr = train.loc[train_mask, use_cols], train.loc[train_mask, TARGET]
Xva, yva = train.loc[val_mask, use_cols], train.loc[val_mask, TARGET]

final_model = CatBoostRegressor(
    loss_function="RMSE", learning_rate=0.05, depth=8, l2_leaf_reg=6.0,
    iterations=8000, random_seed=42, eval_metric="RMSE", early_stopping_rounds=300, verbose=200
)
final_model.fit(
    Pool(Xtr, ytr, cat_features=[Xtr.columns.get_loc(c) for c in cat_cols if c in Xtr.columns]),
    eval_set=Pool(Xva, yva, cat_features=[Xva.columns.get_loc(c) for c in Xva.columns])
)
pred_val = final_model.predict(Xva)
print("Holdout 2019 RMSLE:", rmsle(yva, pred_val))
print("Holdout 2019 MAPE:", mape(yva, pred_val))
