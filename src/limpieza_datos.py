#%%
import pandas as pd

df=pd.read_csv("ventas_raw.csv")
df
# %%
df.columns=df.columns.str.lower().str.strip()
# %%
df["fecha"]=pd.to_datetime(df["fecha"], errors="coerce", dayfirst=True)
df
# %%
df = df.dropna(subset=["fecha"])
df
# %%
df["categoria"] = (
    df["categoria"]
    .str.lower()
    .str.strip()
    .str.replace("á", "a")
    .str.replace("é", "e")
    .str.replace("í", "i")
    .str.replace("ó", "o")
    .str.replace("ú", "u")
)
df.dtypes
# %%
df=df[(df["cantidad"] > 0 ) & (df["precio_unitario"] > 0 )]
df
# %%
df=df.drop_duplicates()
df
# %%
df["total"] = df["cantidad"] * df["precio_unitario"]
df
# %%
df = df.sort_values("fecha")
print(f"Registros después de limpieza: {len(df)}")
# %%
df.to_excel("ventas_limpias.xlsx", index=False)
print("Limpieza completada correctamente")
# %%
print(df.head())
print(df.describe())
# %%
