
#importaciones 
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from fastapi import FastAPI

# Carga del conjunto de datos limpio y revisado (ETL-EDA): Proyecto1.ipynb
df_filtrado = pd.read_csv("df_movies_clean.csv", low_memory=False)

# Inicializamos la app FastApi
app = FastAPI()

# Rutas y Funciones de la API
@app.get('/')
def read_root():
    return {"message": "PROYECTO INDIVIDUAL Nº1 --> agregue '/docs' a la url para continuar"}


# Retorna la cantidad de películas estrenadas en un idioma específico.
@app.get('/peliculas_idioma')
def peliculas_idioma(Idioma: str):
    peliculas_en_idioma = df_filtrado[df_filtrado['spoken_languages'].str.contains(Idioma, case=False)]
    cantidad_peliculas = len(peliculas_en_idioma)
    return f"{cantidad_peliculas} películas fueron estrenadas en {Idioma}"

# Retorna la duración y el año de una película dada
@app.get('/peliculas_duracion')
def peliculas_duracion(Pelicula: str):
    pelicula_info = df_filtrado[df_filtrado['title'] == Pelicula]
    if len(pelicula_info) == 0:
        return "Película no encontrada"
    duracion = pelicula_info.iloc[0]['runtime']
    año = pelicula_info.iloc[0]['release_year']
    return f"Duración: {duracion}. Año: {año}"

# Retorna la cantidad y de películas y la ganancia total de una franquicia dada
@app.get('/franquicia')
def franquicia(Franquicia: str):
    franquicia_info = df_filtrado[df_filtrado['belongs_to_collection'].str.contains(Franquicia, case=False)]
    if len(franquicia_info) == 0:
        return "Franquicia no encontrada"
    cantidad_peliculas = len(franquicia_info)
    ganancia_total = franquicia_info['revenue'].sum()
    ganancia_promedio = ganancia_total / cantidad_peliculas
    return f"La franquicia {Franquicia} posee {cantidad_peliculas} peliculas, una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"

# Retorna la cantidad de películas producidas en un país dado
@app.get('/peliculas_pais')
def peliculas_pais(Pais: str):
    peliculas_en_pais = df_filtrado[df_filtrado['production_countries'].str.contains(Pais, case=False)]
    cantidad_peliculas = len(peliculas_en_pais)
    return f"Se produjeron {cantidad_peliculas} películas en el país {Pais}"

# Retorna la ganancia y cantidad de películas de una productora dada
@app.get('/productoras_exitosas')
def productoras_exitosas(Productora: str):
    productora_info = df_filtrado[df_filtrado['production_companies'].str.contains(Productora, case=False)]
    if len(productora_info) == 0:
        return "Productora no encontrada"
    revenue_total = productora_info['revenue'].sum()
    cantidad_peliculas = len(productora_info)
    return f"La productora {Productora} ha tenido un revenue de {revenue_total} en {cantidad_peliculas} películas"

# Retorna el éxito promedio y una lista con las películas de un director dado
@app.get('/get_director')
def get_director(nombre_director: str):
    director_info = df_filtrado[df_filtrado['crew'].str.contains(nombre_director, case=False)]
    if len(director_info) == 0:
        return "Director no encontrado"
    exito = director_info['popularity'].mean()  # Calcula el promedio de popularidad de las películas del director
    peliculas_info = []
    for index, row in director_info.iterrows():
        pelicula = {
            'nombre': row['title'],
            'fecha_lanzamiento': row['release_date'],
            'retorno': row['return'],
            'costo': row['budget'],
            'ganancia': row['revenue']
        }
        peliculas_info.append(pelicula)
    return {
        'exito': exito,
        'peliculas': peliculas_info
    }

# Devuelve una lista de películas similares a una película dada.
@app.get("/similar_movies/{movie_title}")
async def get_similar_movies_api(movie_title: str):
    similar_movies = get_similar_movies(movie_title)
    return {"similar_movies": similar_movies.tolist()}


# Crear la matriz TF-IDF para el contenido
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df_filtrado['title'])

# Calcular la similitud coseno entre las películas
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_similar_movies(title, cosine_sim=cosine_sim):
    idx = df_filtrado[df_filtrado['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Obtener las 5 películas más similares
    movie_indices = [score[0] for score in sim_scores]
    return df_filtrado['title'].iloc[movie_indices]