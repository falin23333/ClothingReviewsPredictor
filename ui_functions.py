import streamlit as st
import pickle
import pickle
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.model_selection import learning_curve
from sklearn.model_selection import train_test_split
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords 

"""
import pandas as pd
from streamlit_lottie import st_lottie
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import plotly.express as px
import requests
import ui_functions
import nltk
from nltk.stem import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
"""





stopwords_english = stopwords.words('english')


def load_model_and_textinput():
   
    # Agregar un cuadro de texto
    user_input = st.text_input(":green[Copy your review of ChatGPT here or write one yourself., press Enter:]")

    with open(f'models/Vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
        

    with open(f'models/NLP_ratings.pkl', 'rb') as f:
        model = pickle.load(f)
        
     
    if user_input != "":
        preprocessed_review = clean_text(user_input)
        preprocessed_review = vectorizer.transform([preprocessed_review])
        predicted_score = model.predict(preprocessed_review)
        
        
        st.subheader(f":green[Predicted score:] :red[{predicted_score[0]}]⭐️")
        #ui_functions.predict_Recommend_ind(preprocessed_review)
    


def clean_text(text):
    # Convertir todo el texto a minúsculas
    text = text.lower()
    # Remover caracteres especiales
    text = re.sub(r'\W', ' ', text)
    # Remover caracteres simples
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)
    # Remover caracteres simples del inicio
    text = re.sub(r'\^[a-zA-Z]\s+', ' ', text) 
    # Remover múltiples espacios con uno solo
    text = re.sub(r'\s+', ' ', text, flags=re.I)
    # Tokenizar el texto
    text = word_tokenize(text)
    # Remover stopwords
    text = [word for word in text if not word in stopwords_english]
    # Unir las palabras
    text = ' '.join(text)
    #stemmer
    porter = PorterStemmer()
    porter.stem(text)
    return text