import pandas as pd

def cargar():
    return pd.read_csv("ventas.csv")

def validos(df, sede):
    return df[(df["sede"] == sede) & (df["estado"] != "anulado")]

def ingreso_real(df, sede):
    return int(validos(df, sede)["valor"].sum())

def pedidos_validos(df, sede):
    return len(validos(df, sede))
