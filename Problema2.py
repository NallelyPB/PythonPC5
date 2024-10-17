import pandas as pd
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Paso 1: Leer los archivos CSV
df_wines = pd.read_csv('winemag-data-130k-v2.csv')
df_paises = pd.read_csv('paises.csv')

# Paso 2: Renombrar columnas en df_wines
df_wines.rename(columns={
    'country': 'pais',
    'points': 'puntuacion',
    'price': 'precio',
    'variety': 'variedad',
    'winery': 'bodega',
    'description': 'descripcion',
    'designation': 'designacion',
    'taster_name': 'nombre_catador'
}, inplace=True)

# Paso 3: Hacer el merge con df_paises
df_merged = df_wines.merge(df_paises, left_on='pais', right_on='nombre', how='left')

# Crear nuevas columnas
df_merged['precio_categoria'] = df_merged['precio'].apply(lambda x: 'alto' if x > 30 else 'bajo')

def clasificar_puntuacion(puntuacion):
    if puntuacion >= 90:
        return 'Excelente'
    elif puntuacion >= 85:
        return 'Bueno'
    else:
        return 'Promedio'

df_merged['categoria_puntuacion'] = df_merged['puntuacion'].apply(clasificar_puntuacion)

# Paso 4: Generar reportes

# Reporte 1: Vinos mejor puntuados por continente
reporte_1 = df_merged.groupby('continente').agg(mejor_puntuacion=('puntuacion', 'max')).reset_index()
print("\nReporte 1: Vinos mejor puntuados por continente:")
print(reporte_1)

# Reporte 2: Promedio de precio y cantidad de reviews por país
reporte_2 = df_merged.groupby('pais').agg(promedio_precio=('precio', 'mean'), cantidad_reviews=('descripcion', 'count')).reset_index()
reporte_2.sort_values(by='promedio_precio', ascending=False, inplace=True)
print("\nReporte 2: Promedio de precio y cantidad de reviews por país:")
print(reporte_2)

# Reporte 3: Conteo de vinos por categoría de puntuación
reporte_3 = df_merged['categoria_puntuacion'].value_counts().reset_index()
reporte_3.columns = ['categoria_puntuacion', 'conteo']
print("\nReporte 3: Conteo de vinos por categoría de puntuación:")
print(reporte_3)

# Reporte 4: Vinos con precio alto y buena puntuación
reporte_4 = df_merged[(df_merged['precio_categoria'] == 'alto') & (df_merged['puntuacion'] >= 85)]
print("\nReporte 4: Vinos con precio alto y buena puntuación:")
print(reporte_4[['bodega', 'pais', 'puntuacion', 'precio']])

# Paso 5: Exportar reportes a diferentes formatos

# Exportar Reporte 1 a CSV
reporte_1.to_csv('reporte_1_vinos_mejor_puntuados_por_continente.csv', index=False)

# Exportar Reporte 2 a Excel
reporte_2.to_excel('reporte_2_promedio_precio_y_cantidad_reviews_por_pais.xlsx', index=False)

# Exportar Reporte 3 a SQLite
conn = sqlite3.connect('vinos.db')
reporte_3.to_sql('reporte_3_conteo_categoria', conn, if_exists='replace', index=False)
conn.close()

# Exportar Reporte 4 a JSON
reporte_4.to_json('reporte_4_vinos_precio_alto.json', orient='records', lines=True)

print("\nReportes exportados exitosamente.")

# Paso 6: Enviar el Reporte 1 por correo
def enviar_correo(reporte_path, destinatario):
    # Configurar el servidor SMTP
    smtp_server = 'smtp.gmail.com'  # Cambiar si uso otro servidor
    smtp_port = 587
    sender_email = 'nallelyparedes6@gmail.com'  #dirección de correo
    sender_password = '----'  #contraseña

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = sender_email
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Reporte de Vinos Mejor Puntuados por Continente'

    # Cuerpo del mensaje
    cuerpo = 'Adjunto encontrarás el reporte de vinos mejor puntuados por continente.'
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo
    adjunto = MIMEBase('application', 'octet-stream')
    with open(reporte_path, 'rb') as archivo_adjunto:
        adjunto.set_payload(archivo_adjunto.read())
    encoders.encode_base64(adjunto)
    adjunto.add_header('Content-Disposition', f'attachment; filename={reporte_path.split("/")[-1]}')
    mensaje.attach(adjunto)

    # Enviar el correo
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Usar TLS
            server.login(sender_email, sender_password)
            server.send_message(mensaje)
            print("\nCorreo enviado exitosamente.")
    except Exception as e:
        print(f"\nError al enviar el correo: {e}")

# Llamar a la función para enviar el correo con el Reporte 1
enviar_correo('reporte_1_vinos_mejor_puntuados_por_continente.csv', 'alonsopaco2022@gmail.com')





