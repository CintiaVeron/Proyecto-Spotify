# Projecto Spotify

En este Proyecto se analizará en pyhton un dataset de spotify.
Para comenzar tendremos  que realizar un proceso de ETL(Extracción Transform and Load)  y EDA (Exploraty Data Analysis)

ETL
Extract (Extraer): Se descargó un dataset de la web de kaggle, y se lo cargo  en python con la Biblioteca pandas
Dataset link
https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023

Transform (Transformar): para la etapa de transformación se analizaron los tipos de datos de las columnas , se eliminaron valores nulos , y se creo un dataframe solo con las columnas necesarias , las cuales se sometieron al cambio de nombres para que la compresión del código sea mas fácil.
columnas Iniciales:


Load (Cargar): En la etapa final, los datos transformados se cargan en otro archivo csv listo para su uso.

EDA
para esta etapa sobre el proyecto se hicieron varios analisis con el dataset dentro de los cuales son:
Se incluyen graficos con con la libreria matplotlib.pyplot
Se realizó un ranking de las 10 canciones
La cantidad de canciones por año
años con mas cantidad de temas
Se asignó géneros musicales segun los BPM siguiendo esta norma:
Genero segun bpm
R&B: 75 BPM (Género lento, marcado por notas largas
RAP: 90 BPM
HIP-HOP: 100 BPM
REGGAE: 100 BPM
CUMBIA: 90 BPM
POP/ROCK/DANCE: 120 BPM
HEAVY METAL/ PUNK: 140 BPM
y se realizo grafico con la cantidad de canciones segun genero musical 


Caracteristicas del dataset

Características clave:
track_name: nombre de la canción
artista(s)_name: Nombre del artista(s) de la canción
artista_count: Número de artistas que contribuyen a la canción.
released_year: año en que se lanzó la canción.
released_month: Mes en el que se lanzó la canción.
released_day: Día del mes en que se lanzó la canción.
in_spotify_playlists: Número de listas de reproducción de Spotify en las que está incluida la canción
in_spotify_charts: Presencia y ranking de la canción en las listas de Spotify
transmisiones: Número total de transmisiones en Spotify
in_apple_playlists: número de listas de reproducción de Apple Music en las que está incluida la canción
in_apple_charts: Presencia y rango de la canción en las listas de Apple Music
in_deezer_playlists: Número de listas de reproducción de Deezer en las que está incluida la canción
in_deezer_charts: Presencia y rango de la canción en las listas de Deezer
in_shazam_charts: Presencia y rango de la canción en las listas de Shazam
bpm: pulsaciones por minuto, una medida del tempo de la canción.
clave: Clave de la canción
modo: Modo de la canción (mayor o menor)
danceability_%: Porcentaje que indica qué tan adecuada es la canción para bailar
valence_%: Positividad del contenido musical de la canción.
energía_%: Nivel de energía percibido de la canción.
acusticness_%: Cantidad de sonido acústico en la canción.
instrumentalness_%: Cantidad de contenido instrumental en la canción.
liveness_%: Presencia de elementos de actuación en vivo.
Speechiness_%: cantidad de palabras habladas en la canción.
