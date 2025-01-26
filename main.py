#Librerias
import os #para verificar la dirección del archivo es correcta
import math # Importar el módulo math para acceder a funciones matemáticas básicas como sqrt(), sin(), cos(), entre otras.
import string # Importar la librería string para trabajar con cadenas de caracteres
import numpy as np #cálculo numérico que proporciona funciones y herramientas para trabajar con matrices y vectores de gran tamaño y alta dimensionalidad
import pandas as pd #para el análisis y la manipulación de datos
import networkx as nx #para trabajar con grafos y redes complejas, manipulación y análisis de estructuras de redes
import matplotlib.pyplot as plt # Librería para crear gráficos en Python
import seaborn as sns # Librería para crear visualizaciones estadísticas más complejas
import nltk #(Natural Language Toolkit) para procesamiento de lenguaje natural
from wordcloud import WordCloud #Para crear nubes de palabras a partir de un texto
from collections import defaultdict

nltk.download('punkt') # "punkt" Es un tokenizer muy popular y eficaz que se utiliza para dividir el texto en oraciones y palabras
nltk.download('stopwords') # "stopwords" Filtra palabras vacias como conectores

# Importar la función word_tokenize de la librería nltk.tokenize y el corpus de stopwords de la librería nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#Algunas listas para filtrar plabras sin sentido en los textos
stopwords_es = set(stopwords.words('spanish')) # Definir una lista de palabras vacías ('stopwords') en español utilizando la librería NLTK
abecedario = list(string.ascii_lowercase) # Crear una lista con las letras del alfabeto en minúscula utilizando la librería string
random_words = ['uniandeseduco', 'cr', 'abc','in', 'siempre','enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre', 'día', 'mes', 'año', 'wwwbienestarunaleduco', 'bienestarbogotaunaleducoadjuntos__rompiendo', 'va', 'i', 'ii', 'iii', 'vi', 'debe', 'v', 'iv', 'vii', 'vii', 'ix', 'to', 'nº', 'pro', 'na', 'nas', 'pag', 'http', 'sf','co', 'así', 'sí','cada','si','través', 'ser', 'wwwwomenslinkworldwideorgwlwbajarfs', 'omegsdmujergovcoindexphparticulosviolenciasdigitalesgroomingsextorsionciberacosoyphishing', 'lynett']


