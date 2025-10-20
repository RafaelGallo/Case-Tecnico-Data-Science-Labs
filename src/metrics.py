# src/metrics.py
import numpy as np
from sklearn.model_selection import GroupKFold
import numpy as np, pandas as pd

def rmsle(y_true, y_pred):
    # cuidado com zeros/negativos
    y_true = np.clip(y_true, a_min=0, a_max=None)
    y_pred = np.clip(y_pred, a_min=0, a_max=None)
    return np.sqrt(np.mean(np.square(np.log1p(y_pred) - np.log1p(y_true))))

def mape(y_true, y_pred, eps=1e-7):
    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)
    mask = y_true != 0
    return np.mean(np.abs((y_true[mask] - y_pred[mask]) / (y_true[mask] + eps))) * 100

TARGET = "TradePrice"

cat_cols = [
    "Type","Region","Prefecture","Municipality","DistrictName","NearestStation",
    "Structure","Use","Purpose","Direction","DirSimple","Classification",
    "CityPlanning","FloorPlan","LandShape","Renovation"
]
num_cols = [
    "Area","LogArea","TotalFloorArea","LogTotalFloorArea",
    "Frontage","Breadth",
    "CoverageRatio","FloorAreaRatio","FAR_to_Coverage",
    "MinTimeToNearestStation","MaxTimeToNearestStation","MeanTimeToStation",
    "AgeAtSale","UnitPrice","PricePerTsubo",
    "AreaIsGreaterFlag","FrontageIsGreaterFlag","TotalFloorAreaIsGreater",
    "PrewarBuilding","HasPrivateRoad","IsRenovated","Year","Quarter"
]

use_cols = [c for c in (cat_cols + num_cols) if c in train.columns]

X = train[use_cols].copy()
y = train[TARGET].values
groups = train["Year"].values
