# 🏠 EDA — Referencia del Precio del Alquiler en España

## 📌 Descripción del Proyecto

Este proyecto consiste en la realización de un **Exploratory Data Analysis (EDA)** sobre el mercado del alquiler en España utilizando el dataset oficial:

> **“Referencia del Precio del Alquiler de Vivienda”**  
> Fuente: datos.gob.es

El objetivo principal del proyecto es analizar la evolución y distribución del precio del alquiler en España, identificando patrones territoriales, diferencias entre provincias y tendencias temporales.

---

## 🎯 Problem Statement

> *¿Qué variables explican mejor el precio del alquiler en España y cómo varían según la ubicación y el tipo de vivienda?*

---

## Objetivos Específicos

- Detectar diferencias territoriales en el precio del alquiler.
- Analizar la evolución histórica del alquiler.
- Identificar provincias y municipios con precios más elevados.
- Detectar posibles desigualdades territoriales.
- Analizar tendencias y distribuciones del mercado inmobiliario.

---

## 🧠 Hipótesis y Resultados

| Hipótesis | Enunciado | Resultado |
|-----------|-----------|-----------|
| H1 | Las grandes provincias tienen precios significativamente superiores | ⚠️ Parcialmente confirmada — Bizkaia y Gipuzkoa superan a Madrid y Barcelona |
| H2 | Existe una desigualdad territorial clara entre comunidades autónomas | ✅ Confirmada — la brecha entre provincias caras y baratas es muy pronunciada |
| H3 | El precio del alquiler ha aumentado progresivamente con los años | ✅ Confirmada — el índice de 2024 es el más alto de la serie histórica |
| H4 | El tipo de vivienda influye en el precio del alquiler | ⚠️ Confirmada con matiz — la unifamiliar tiene mayor precio y variabilidad |

---

## 📂 Dataset Utilizado

- **Fuente:** [datos.gob.es — Referencia del Precio del Alquiler de Vivienda](https://datos.gob.es/es/catalogo/e05233601-referencia-del-precio-del-alquiler-de-vivienda)
- **Archivo principal:** `VDP001_01.csv`
- **Período:** 2011–2024
- **Cobertura:** todas las provincias y municipios de España

---

### 📊 Variables principales

| Variable | Descripción |
|----------|-------------|
| `PROVINCIA` | Provincia española |
| `NOMBRE_MUNICIPIO` | Nombre del municipio |
| `COD_POSTAL` | Código postal |
| `ELEMENTO` | Tipo de métrica analizada |
| `TIPO_VIVIENDA` | Colectiva o Unifamiliar |
| `TIPO_MEDIDA` | Tipo estadístico de la medida |
| `AÑO` | Año de referencia |
| `VALOR` | Índice de precio mediano |

---
##  Principales Hallazgos

- **El índice de precio en 2024 es el más alto de toda la serie histórica**, superando incluso los valores previos a la crisis de 2008. La aceleración entre 2020 y 2024 es la más intensa del período analizado.
- **Bizkaia (≈640) y Gipuzkoa (≈600) son las provincias más caras**, por encima de Madrid y Barcelona (≈510). Este es el hallazgo más sorprendente del análisis.
- **La desigualdad territorial es enorme.** Las provincias del interior (Teruel, Ávila, Badajoz, Lugo) presentan índices que representan menos de la mitad de los valores del País Vasco.
- **La vivienda unifamiliar sube más y llega más alto.** Desde 2019, el gap entre unifamiliar y colectiva se amplía, y los outliers de unifamiliar alcanzan valores de 2.200+ en 2024.
- **La correlación entre año y precio es baja (r=0,19)**, lo que indica que la ubicación geográfica es el factor dominante, no el tiempo.
- **Madrid y Barcelona destacan por su dispersión interna**: conviven municipios con precios moderados y zonas de lujo extremo dentro de la misma provincia.

---

## 📁 Estructura del Repositorio

```
EDA_Alquiler_Vivienda_Espana/
│
├── src/
│   ├── data/
│   │     ├── processed/                      # Dataset limpio listo para análisis
│   │     └── raw/                            # Dataset original sin modificar
│   │ 
│   ├── docs/                                 # Documentos extras usados de apoyo en las tareas
│   │ 
│   │
│   ├── img/                                  # Gráficos exportados del análisis
│   │
│   ├── notebooks/
│   │     ├── 01_data_cleaning.ipynb          # Limpieza y preparación de datos
│   │     └── 02_eda_analysis.ipynb           # Análisis univariante y bivariante
│   │ 
│   └── utils/ 
│ 
├──.gitattributes
├──.gitignore
├── README.md
├── main.ipynb
├── memoria_EDA.pdf
├── presentación.pdf
└── requirements.txt

```
---

## 🛠️ Tecnologías Utilizadas

- **Python 3.10+**
- **Pandas** — manipulación y análisis de datos
- **NumPy** — operaciones numéricas
- **Matplotlib** — visualizaciones base
- **Seaborn** — visualizaciones estadísticas
- **Jupyter Notebook** — entorno de desarrollo
- **Canva** - slides para presentación

---

## 👥 Equipo y División del Trabajo

| Persona | Rol | Responsabilidades |
|---------|-----|-------------------|
| Nil Coronado| Data Acquisition & Cleaning | Carga del dataset, limpieza, data dictionary |
| Enrique Algarra | EDA & Visualización | Análisis exploratorio, gráficos, heatmaps |
| Lucía Vetrano| Business Insights & Storytelling | Main, memoria del proyecto , presentación, conclusiones, vídeo |

---
