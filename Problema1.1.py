# Importar las librerías necesarias
import pandas as pd

# Leer el archivo CSV
df_airbnb = pd.read_csv("airbnb.csv")

# 1. Mostrar las primeras filas del dataframe
print("Primeras 5 filas del dataset:")
print(df_airbnb.head())

# 2. Tamaño del dataframe (filas, columnas)
print("\nTamaño del dataset (filas, columnas):")
print(df_airbnb.shape)

# 3. Listar los nombres de las columnas
print("\nNombres de las columnas:")
print(df_airbnb.columns)

# 4. Información general del dataframe (tipos de datos y valores nulos)
print("\nInformación general del dataset:")
print(df_airbnb.info())

# 5. Estadísticas descriptivas de las columnas numéricas
print("\nEstadísticas descriptivas de las columnas numéricas:")
print(df_airbnb.describe())

# 6. Verificar la existencia de valores nulos en el dataset
print("\nValores nulos por columna:")
print(df_airbnb.isnull().sum())

# 7. Explorar la distribución de los tipos de propiedad (room_type)
print("\nDistribución de los tipos de propiedad:")
print(df_airbnb['room_type'].value_counts())

# 8. Verificar los diferentes barrios/neighborhood
print("\nBarrios disponibles en los datos:")
print(df_airbnb['neighborhood'].unique())

# 9. Promedio de la puntuación de satisfacción
print("\nPromedio de la satisfacción general:")
print(df_airbnb['overall_satisfaction'].mean())

# 10. Precio máximo, mínimo y promedio
print("\nPrecio máximo, mínimo y promedio de los alojamientos:")
print(f"Precio máximo: {df_airbnb['price'].max()} euros")
print(f"Precio mínimo: {df_airbnb['price'].min()} euros")
print(f"Precio promedio: {df_airbnb['price'].mean()} euros")