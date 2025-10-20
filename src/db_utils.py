# src/db_utils.py
from sqlalchemy import create_engine

def get_engine(db_path="db/tokyo.sqlite"):
    return create_engine(f"sqlite:///{db_path}", future=True)
