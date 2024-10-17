import pandas as pd

# Cargar el dataset
df_airbnb = pd.read_csv("airbnb.csv")

# Mostrar las primeras filas para verificar que se ha cargado correctamente
print("Primeras filas del DataFrame:")
print(df_airbnb.head())

# Filtrar los datos de Roberto y Clara usando sus IDs
roberto_id = 97503
clara_id = 90387

# Crear un nuevo DataFrame con las propiedades de ambos
df_roberto_clara = df_airbnb[(df_airbnb['room_id'] == roberto_id) | (df_airbnb['room_id'] == clara_id)]

# Verificar el DataFrame filtrado
print("\nDataFrame con las propiedades de Roberto y Clara:")
print(df_roberto_clara)

# Guardar el DataFrame en un archivo Excel
df_roberto_clara.to_excel('roberto.xlsx', index=False)

print("\nEl DataFrame ha sido creado y guardado como 'roberto.xls'.")