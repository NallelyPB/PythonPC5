import pandas as pd

# Cargar el dataset
df_airbnb = pd.read_csv("airbnb.csv")

# Mostrar las primeras filas para verificar que se ha cargado correctamente
print("Primeras filas del DataFrame:")
print(df_airbnb.head())

# Definir el presupuesto y la duración de la estancia
presupuesto = 50
noches = 3
costo_total = presupuesto * noches  # Costo total que puede gastar

# Filtrar las propiedades que cumplen con el presupuesto
df_filtrado = df_airbnb[df_airbnb['price'] <= costo_total]

# Filtrar las propiedades que son habitaciones compartidas
df_compartidas = df_filtrado[df_filtrado['room_type'] == 'Shared room']

# Ordenar las propiedades por puntuación y luego por precio
df_compartidas_sorted = df_compartidas.sort_values(by=['overall_satisfaction', 'price'], ascending=[False, True])

# Seleccionar las 10 propiedades más baratas
top_10_propiedades = df_compartidas_sorted.head(10)

# Mostrar el resultado
print("\nLas 10 propiedades más baratas para Diana:")
print(top_10_propiedades[['room_id', 'room_type', 'neighborhood', 'reviews', 'overall_satisfaction', 'accommodates', 'bedrooms', 'price']])