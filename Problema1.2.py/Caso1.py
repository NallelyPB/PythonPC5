import pandas as pd

# Cargar los datos del archivo CSV
df_airbnb = pd.read_csv("airbnb.csv")

# Filtrar por las condiciones especificadas
df_filtrado = df_airbnb[
    (df_airbnb['accommodates'] >= 4) &            # Acomoda al menos 4 personas
    (df_airbnb['reviews'] > 10) &                 # Más de 10 reseñas
    (df_airbnb['overall_satisfaction'] > 4)       # Puntuación mayor a 4
]

# Ordenar por satisfacción de mayor a menor, y en caso de empate, por número de reseñas
df_ordenado = df_filtrado.sort_values(
    by=['overall_satisfaction', 'reviews'], 
    ascending=[False, False]
)

# Seleccionar las 3 mejores alternativas
top_3_alternativas = df_ordenado.head(3)

# Mostrar las 3 alternativas
print(top_3_alternativas[['room_id', 'room_type', 'neighborhood', 'reviews', 'overall_satisfaction', 'accommodates', 'bedrooms', 'price']])