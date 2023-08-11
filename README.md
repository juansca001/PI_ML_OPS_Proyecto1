# Proyecto Individual Nº1 - Recomendación de Películas

Este proyecto se enfoca en la construcción de un sistema de recomendación de películas utilizando técnicas de procesamiento de lenguaje natural (NLP) y el framework FastAPI para crear una API accesible. A continuación, se proporciona una descripción general del proyecto, la estructura de archivos en el repositorio de GitHub.

## Descripción General

El objetivo de este proyecto es desarrollar un sistema de recomendación de películas basado en el contenido de sus títulos y otros atributos relacionados. El proceso implica la realización de tareas de Extracción, Transformación y Carga (ETL), así como Análisis Exploratorio de Datos (EDA) para entender mejor los datos. Luego, se implementa una API utilizando el framework FastAPI para acceder a funciones específicas de recomendación y análisis.

## Estructura de Archivos en el Repositorio

El repositorio de GitHub contiene los siguientes archivos:

1. `movies_dataset.csv`: Dataset que contiene los datos de las películas, utilizado como entrada para el proyecto.
2. `credits.csv`: Dataset con información de los créditos de las películas.
3. `Proyecto1.ipynb`: Archivo Jupyter Notebook que contiene el código documentado para las tareas de ETL y EDA.
4. `deploy.py`: Archivo Python que implementa la API utilizando FastAPI con las funciones de recomendación y análisis.

## Notas para la ejecución del Proyecto
El archivo deploy.py contiene el código necesario para inicializar la API FastAPI y definir las rutas que ofrecen funcionalidades como obtener películas en un idioma específico, detalles de una película, información de franquicias, y más. Además, se calcula la matriz TF-IDF y la similitud coseno para recomendar películas similares.

Para obtener más detalles sobre las rutas y funciones disponibles, así como para probarlas a través de la interfaz interactiva de documentación de FastAPI, ejecuta la aplicación y accede a /docs en la URL.

Nota: Para desplegar y hacer que la API sea accesible públicamente, deberás seguir los pasos adecuados de implementación y alojamiento, que pueden incluir la selección de un servidor web o plataforma en la nube y la configuración de los puertos y direcciones IP permitidos.




User
Pasa el contenido anterior en formato .md para crear el readme
ChatGPT
Claro, aquí tienes el contenido en formato Markdown para crear el README:

markdown
Copy code
# Proyecto Individual Nº1 - Recomendación de Películas

Este proyecto se enfoca en la construcción de un sistema de recomendación de películas utilizando técnicas de procesamiento de lenguaje natural (NLP) y el framework FastAPI para crear una API accesible. A continuación, se proporciona una descripción general del proyecto, la estructura de archivos en el repositorio de GitHub y el contenido del archivo `deploy.py` que contiene la implementación de la API.

## Descripción General

El objetivo de este proyecto es desarrollar un sistema de recomendación de películas basado en el contenido de sus títulos y otros atributos relacionados. El proceso implica la realización de tareas de Extracción, Transformación y Carga (ETL), así como Análisis Exploratorio de Datos (EDA) para entender mejor los datos. Luego, se implementa una API utilizando el framework FastAPI para acceder a funciones específicas de recomendación y análisis.

## Estructura de Archivos en el Repositorio

El repositorio de GitHub contiene los siguientes archivos:

1. `movies_dataset.csv`: Dataset que contiene los datos de las películas, utilizado como entrada para el proyecto.
2. `credits.csv`: Dataset con información de los créditos de las películas.
3. `Proyecto1.ipynb`: Archivo Jupyter Notebook que contiene el código documentado para las tareas de ETL y EDA.
4. `deploy.py`: Archivo Python que implementa la API utilizando FastAPI con las funciones de recomendación y análisis.

## Ejecución del proyecto

El archivo deploy.py contiene el código necesario para inicializar la API FastAPI y definir las rutas que ofrecen funcionalidades como obtener películas en un idioma específico, detalles de una película, información de franquicias, y más. Además, se calcula la matriz TF-IDF y la similitud coseno para recomendar películas similares.

Para obtener más detalles sobre las rutas y funciones disponibles, así como para probarlas a través de la interfaz interactiva de documentación de FastAPI, ejecuta la aplicación y accede a /docs en la URL.

Nota: Para desplegar y hacer que la API sea accesible públicamente, deberás seguir los pasos adecuados de implementación y alojamiento, que pueden incluir la selección de un servidor web o plataforma en la nube y la configuración de los puertos y direcciones IP permitidos.

## Fuente de datos
Carpeta con los 2 archivos con datos que requieren ser procesados (movies_dataset.csv y credits.csv), tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).

Nota: Debido a que los Dataset son muy pesados deben descargarlos del siguiente link y guardarlos en la misma carpeta de este proyecto.

https://drive.google.com/drive/folders/1mfUVyP3jS-UMdKHERknkQ4gaCRCO2e1v 





