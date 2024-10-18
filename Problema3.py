import os
import zipfile
import requests
import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

# Paso 1: Descargar el archivo .zip desde la URL solo si no existe
def descargar_zip(url, destino):
    if not os.path.exists(destino):
        response = requests.get(url)
        with open(destino, 'wb') as file:
            file.write(response.content)
        print(f"Archivo descargado en: {destino}")
    else:
        print(f"El archivo {destino} ya existe, no se descargará nuevamente.")

# Paso 2: Descomprimir el archivo .zip
def descomprimir_zip(ruta_zip, ruta_destino):
    with zipfile.ZipFile(ruta_zip, 'r') as zip_ref:
        zip_ref.extractall(ruta_destino)
    print(f"Archivos descomprimidos en: {ruta_destino}")

# Paso 3: Leer uno de los archivos descomprimidos usando pandas
def leer_archivo_pandas(ruta_archivo):
    df = pd.read_csv(ruta_archivo, sep='\t', header=None)
    print("Datos leídos del archivo:")
    print(df.head())
    return df

# Paso 4: Renombrar las columnas y quedarnos con las necesarias
def procesar_datos(df):
    df_filtrado = df[[0, 2, 3, 5, 6]]  # Seleccionamos las columnas necesarias
    df_filtrado.columns = ['VideoID', 'Age', 'Category', 'Views', 'Rate']  # Renombramos las columnas
    print("\nDatos filtrados:")
    print(df_filtrado.head())
    
    # Filtrar por una categoría específica (ejemplo: Music)
    df_filtrado = df_filtrado[df_filtrado['Category'] == 'Music']
    print("\nDatos filtrados por la categoría 'Music':")
    print(df_filtrado.head())
    
    return df_filtrado

# Paso 5: Exportar datos a MongoDB
def exportar_a_mongodb(df):
    client = MongoClient('mongodb+srv://Nallely:nallely@cluster0.8rpre.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
    db = client['youtube_data']
    collection = db['videos']
    data_dict = df.to_dict("records")
    collection.insert_many(data_dict)
    print("Datos exportados a MongoDB con éxito.")

# Paso 6: Crear gráficos
def crear_graficos(df):
    plt.figure(figsize=(10, 6))
    df.groupby('Category')['Views'].sum().plot(kind='bar')
    plt.title('Visualizaciones por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Visualizaciones')
    plt.show()

    plt.figure(figsize=(10, 6))
    df.groupby('Category')['Rate'].mean().plot(kind='bar')
    plt.title('Calificación Promedio por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Calificación Promedio')
    plt.show()

# Paso 7: Ejecutar el flujo completo
url = 'https://netsg.cs.sfu.ca/youtubedata/0303.zip'
ruta_zip = '0303.zip'
ruta_destino = 'youtube_data'

descargar_zip(url, ruta_zip)
descomprimir_zip(ruta_zip, ruta_destino)

# Verificar los archivos descomprimidos
archivos_descomprimidos = os.listdir(ruta_destino)
print("Archivos descomprimidos:")
for archivo in archivos_descomprimidos:
    print(archivo)

directorio = os.path.join(ruta_destino, archivos_descomprimidos[0])
if os.path.isdir(directorio):
    archivos_dentro = os.listdir(directorio)
    print("\nArchivos dentro del directorio descomprimido:")
    for archivo in archivos_dentro:
        print(archivo)

    ruta_archivo = os.path.join(directorio, archivos_dentro[0])
    df = leer_archivo_pandas(ruta_archivo)

    df_filtrado = procesar_datos(df)

    # Exportar a MongoDB
    exportar_a_mongodb(df_filtrado)

    # Crear gráficos
    crear_graficos(df_filtrado)

    # Compartir enlace
    print(f"Los datos se encuentran en: {url}")
