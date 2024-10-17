import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df_airbnb = pd.read_csv("airbnb.csv")

# Mostrar las primeras filas para verificar que se ha cargado correctamente
print("Primeras filas del DataFrame:")
print(df_airbnb.head())

# --- Agrupamiento 1: Por tipo de propiedad ---

# Agrupamos por tipo de habitación y calculamos el conteo y el precio promedio
agrupamiento_tipo = df_airbnb.groupby('room_type').agg(
    conteo=('room_id', 'count'),
    precio_promedio=('price', 'mean')
).reset_index()

print("\nAgrupamiento por tipo de propiedad:")
print(agrupamiento_tipo)

# Gráfico del agrupamiento por tipo de propiedad
plt.figure(figsize=(10, 5))
sns.barplot(data=agrupamiento_tipo, x='room_type', y='precio_promedio', hue='room_type', palette='viridis', legend=False)
plt.title('Precio Promedio por Tipo de Propiedad')
plt.ylabel('Precio Promedio (€)')
plt.xlabel('Tipo de Propiedad')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Agrupamiento 2: Por barrio ---

# Agrupamos por barrio y calculamos el conteo y la puntuación promedio
agrupamiento_barrio = df_airbnb.groupby('neighborhood').agg(
    conteo=('room_id', 'count'),
    puntuacion_promedio=('overall_satisfaction', 'mean')
).reset_index()

print("\nAgrupamiento por barrio:")
print(agrupamiento_barrio)

# Gráfico del agrupamiento por barrio
plt.figure(figsize=(12, 6))
sns.barplot(data=agrupamiento_barrio, x='puntuacion_promedio', y='neighborhood', hue='neighborhood', palette='magma', legend=False)
plt.title('Puntuación Promedio por Barrio')
plt.ylabel('Barrio')
plt.xlabel('Puntuación Promedio')
plt.tight_layout()
plt.show()