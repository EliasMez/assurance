import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Charger le modèle depuis le fichier
with open("model.pkl", 'rb') as file:
    best_model = pickle.load(file)

st.title("Assur'Aimant")
st.subheader("Faites votre devis d'assurance en 2 minutes !")

# Ajout d'une image
# st.image(image = "/home/apprenant/Bureau/Brief-ML-Assurance/Assuraimant.jpeg")


# Demande des informations à l'utilisateur
age = st.number_input("Quel est votre âge?", min_value=0, max_value=120)
sexe = st.radio("Quel est votre sexe?", ("male", "femelle"))
region = st.selectbox("Quelle est votre région?", ["northeast", "northwest", "southeast", "southwest"])
grade=st.selectbox("Quelle est votre grade?", ["underweight", "good", "overweight", "obesity"])
bmi = st.number_input("Quel est votre IMC?", min_value=0, max_value=50)
nombre_enfants = st.number_input("Combien avez-vous d'enfants?", min_value=0, max_value=20)
fumeur = st.radio("Êtes-vous fumeur?", ("yes", "no"))



liste = [int(age), sexe,region,grade, bmi, int(nombre_enfants), fumeur]

liste_col = ['age', 'sex','region','grade','bmi', 'children', 'smoker']

if st.button("Démarrez l'estimation"):
    df = pd.DataFrame(np.array(liste).reshape(1, -1),columns = liste_col)

    charges = int(best_model.predict(df))
    st.success("Votre estimation est de {} $".format(charges))