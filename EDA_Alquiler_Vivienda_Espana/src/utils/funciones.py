# Funciones auxiliares del proyecto EDA

import pandas as pd


def cargar_dataset(ruta: str, sep: str = ';') -> pd.DataFrame:
    """Carga el dataset desde la ruta indicada."""
    df = pd.read_csv(ruta, sep=sep)
    df.columns = [c.strip().upper().replace(' ', '_') for c in df.columns]
    return df


def filtrar_precio_mediano(df: pd.DataFrame) -> pd.DataFrame:
    """Filtra el dataset para quedarse solo con el precio mediano por municipio."""
    return df[(df['ELEMENTO'] == 'PRECIO') & (df['TIPO_MEDIDA'] == 'MEDIANA')]


def ranking_provincias(df: pd.DataFrame, top: int = 15) -> pd.Series:
    """Devuelve el ranking de provincias por índice de precio mediano."""
    return df.groupby('PROVINCIA')['VALOR'].median().sort_values(ascending=False).head(top)