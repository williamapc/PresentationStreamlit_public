import streamlit as st


#title = "RECO_PLANTES - Reconnaissance de plants et de leurs maladies.🍎"
sidebar_name = "Introduction"


def run():

    # TODO: choose between one of these GIFs
    st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/1.gif", width=1600)
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif")

    #st.title(title)

    #st.markdown("---")

    st.markdown(
   """
   

              
    # RECO_PLANTES - Reconnaissance de plantes et de leurs maladies :apple:
    Ce projet est réalisé par :
    - Guillaume Audrant
    - Fayçal Djerourou
    
    [![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://github.com/faycal77/reco_plantes.git)
    
    ## Contexte
    
    Le projet _Reco_Plantes_ s'inscrit dans le cadre de la formation
    Datascientest et vise à valider les concepts théoriques d'intelligence
    artificielle (IA) acquis sur un exemple réel.
    
    L'objectif du projet, au delà de la mise en pratique des concepts vus
    lors de la formation, c'est également d'écrire un outil informatique
    en langage python permettant de prendre en entrée un répertoire
    d'images de plusieurs plantes et produit en sortie pour chaque image :
    - :one: le type de la plante,
    - :two: état de la plante (saine ou malade)
    - :three: le type de maladie de la plante au cas où cette dernière est malade
    
    La problématique posée par le projet est donc de type classification
    muti-classes sur laquelle plusieurs techniques d'apprentissage machine
    ont été utilisées.
    
    """
)
