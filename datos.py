import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#ETL Extrac, Transform, Load
data=pd.read_csv("D:/usuarios/CIN/MIS DOCUMENTOS/Proyecto/spotify-2023.csv", delimiter=',',encoding='latin-1')
print(data.isna().sum())
cantidad_de_datos = data.size
print(cantidad_de_datos)
data.dropna(subset=['in_shazam_charts', 'key'], inplace=True)#eliminar valores nulos
print(data.info())

print(data.head(5))
#eliminar columnas innecesarias
columnas_a_eliminar=['in_spotify_charts','in_apple_playlists','in_apple_charts','in_deezer_playlists','in_deezer_charts','in_shazam_charts','key','mode','speechiness_%','liveness_%']
data.drop(columnas_a_eliminar,axis=1,inplace=True)
print(data.info())

#renombrar columnas 

data.rename(columns={'track_name':'Nombre_Cancion'}, inplace=True)
data.rename(columns={'artist_count':'cantidad_artistas'}, inplace=True)
data.rename(columns={'artist(s)_name':'Nombre_Artista'}, inplace=True)
data.rename(columns={'released_year':'anio'}, inplace=True)
data.rename(columns={'released_month':'mes'}, inplace=True)
data.rename(columns={'released_day':'dia'}, inplace=True)
data.rename(columns={'streams':'transmisiones'}, inplace=True)
data.rename(columns={'in_spotify_playlists':'nro_playlist'}, inplace=True)
data.rename(columns={'danceability_%':'%_bailable'}, inplace=True)
data.rename(columns={'valence_%':'%_positividad'}, inplace=True)
data.rename(columns={'energy_%':'%_energia'}, inplace=True)
data.rename(columns={'acousticness_%':'%_sonido_acustico'}, inplace=True)
data.rename(columns={'instrumentalness_%':'%_instrumental'}, inplace=True)

print(data.info())

condicion = (data['bpm'] <= 0) | (data['bpm'] < 60)

# Eliminar las filas que cumplan con la condición
data = data[~condicion]

# Mostrar el DataFrame resultante
print(data)

spotify_df=data





#EDA
# Mostrar las primeras 10 canciones en el ranking

spotify_df= spotify_df.sort_values(by='transmisiones', ascending=False)
spotify_df= spotify_df.reset_index(drop=True)
ranking=spotify_df[['Nombre_Cancion','Nombre_Artista']]
ranking['ranking']=range(1, len(ranking)+1)

top_10 = ranking.head(10)
print(top_10)



#Grafico cantidad de Temas por año 

cantidad_por_anio=spotify_df['anio'].value_counts().sort_index()
#grafico de barras 
plt.figure(figsize=(12, 6))
cantidad_por_anio.plot(kind='bar')
plt.title('Cantidad de Temas por Año')
plt.xlabel('Año de Lanzamiento')
plt.ylabel('Cantidad de Temas')
plt.xticks(rotation=45)
plt.show()
#año con mas cantidad de temas 
anio_max_temas=cantidad_por_anio.idxmax()
max_temas=cantidad_por_anio.max()
print('el año maximo de temas es',anio_max_temas,'con',max_temas,'temas')


# Función para asignar géneros basados en los BPM
def asignar_genero(bpm):
    if bpm < 70:
        return "Blues"
    elif bpm <= 120:
        return "Rock" if bpm <= 100 else "Pop"
    elif bpm <= 160:
        return "Electrónica/Dance" if bpm <= 130 else "Techno" if bpm <= 140 else "Trance"
    else:
        return "Drum and Bass" if bpm <= 160 else "Hardcore"

# Agregar la columna 'Género' utilizando la función apply
spotify_df['Género'] = spotify_df['bpm'].apply(asignar_genero)

# Mostrar el DataFrame con la nueva columna
print(spotify_df)

cantidad_por_genero=spotify_df['Género'].value_counts().sort_index()
#grafico de barras 
plt.figure(figsize=(12, 6))
cantidad_por_genero.plot(kind='bar')
plt.title('Cantidad de Temas por genero')
plt.xlabel('tipo de Genero')
plt.ylabel('Cantidad de Temas')
plt.xticks(rotation=45)
plt.show()




spotify_df.to_csv('archivo_spotify.csv', index=False)