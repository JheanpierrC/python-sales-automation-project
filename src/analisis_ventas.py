#%%
import pandas as pd

df=pd.read_excel("ventas_limpias.xlsx")
df
# %%
ventas_mes=df.groupby(df["fecha"].dt.to_period("M"))["total"].sum()
ventas_mes
# %%
ventas_categoria=df.groupby("categoria")["total"].sum().sort_values(ascending=False)
ventas_categoria
# %%
print("Ventas por mes: ")
print(ventas_mes)
print("Ventas por categorias: ")
print(ventas_categoria)
# %%
