#%%
import pandas as pd

df=pd.read_excel("ventas_limpias.xlsx")
df
# %%
ventas_por_mes = (
    df
    .groupby(df["fecha"].dt.to_period("M"))["total"]
    .sum()
    .reset_index()
)
# %%
ventas_por_mes["fecha"] = ventas_por_mes["fecha"].astype(str)
# %%
ventas_por_categoria = (
    df
    .groupby("categoria")["total"]
    .sum()
    .reset_index()
    .sort_values(by="total", ascending=False)
)
# %%
top_productos = (
    df
    .groupby("producto")["total"]
    .sum()
    .reset_index()
    .sort_values(by="total", ascending=False)
    .head(10)
)
# %%
ruta_salida = "reporte_ventas.xlsx"

# %%
with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Datos Limpios", index=False)
    ventas_por_mes.to_excel(writer, sheet_name="Ventas por Mes", index=False)
    ventas_por_categoria.to_excel(writer, sheet_name="Ventas por Categoria", index=False)
    top_productos.to_excel(writer, sheet_name="Top 10 Productos", index=False)
print("Reporte de ventas generado correctamente")
# %%
