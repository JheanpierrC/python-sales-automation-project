# Proyecto: Limpieza y Análisis de Ventas con Python

Este proyecto tiene como objetivo demostrar habilidades prácticas en **limpieza, transformación y análisis de datos** usando Python.

El flujo simula un escenario real de trabajo como **Analista de Datos Jr / Asistente TI**, donde los datos iniciales presentan errores comunes y deben ser preparados para análisis y reportes.

---

## Objetivo del proyecto

- Limpiar un dataset de ventas con datos inconsistentes
- Estandarizar fechas, precios y cantidades
- Detectar y tratar valores nulos y errores
- Generar métricas básicas para análisis de negocio
- Exportar resultados a Excel para consumo no técnico

---

## Dataset

El dataset contiene **+100 registros** simulados de ventas con las siguientes columnas:

- `order_id`
- `order_date`
- `country`
- `product`
- `quantity`
- `price`
- `payment_status`

Incluye problemas reales como:
- Cantidades en 0
- Precios negativos
- Fechas como texto
- Estados de pago fallidos
- Datos duplicados

---

## Proceso de limpieza

1. Conversión de fechas a formato `datetime`
2. Eliminación de:
   - Cantidades iguales a 0
   - Precios negativos
3. Normalización de textos
4. Eliminación de duplicados
5. Creación de nuevas métricas:
   - Total de venta
   - Ventas agregadas por mes

---

## Análisis generado

- Total de ventas por mes
- Dataset limpio listo para análisis o dashboard
- Exportación automática a archivo Excel con múltiples hojas

---

## Estructura del proyecto
ventas-limpieza-python/
│
├── data/
│ └── ventas.csv
│
├── notebooks/
│ └── limpieza_ventas.ipynb
│
├── output/
│ └── ventas_limpias.xlsx
│
├── README.md
├── requirements.txt


---

## Tecnologías utilizadas

- Python 3
- Pandas
- NumPy
- XlsxWriter

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/ventas-limpieza-python.git
```

2. Instalar dependencias:
pip install -r requirements.txt

3. Ejecutar el notebook limpieza_ventas.ipynb

### Autor ###
Jheanpierr Cobb
Estudiante de Ingeniería de Sistemas
Interés en análisis de datos, automatización y TI aplicada
