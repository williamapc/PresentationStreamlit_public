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
    
    Ce document est organisé en plusieurs sections correspondant aux
    différentes étapes précoisées par la méthodologie data science, à
    savoir :
    - :one: La première section est consacrée à la collecte des
    données.
    - :two: La deuxième section porte sur l'exploration et l'analyse des données récoltées.
    - :three: La section trois aborde les techniques utilisées
    dans le cadre du projet pour la préparation des données.
    - :four: La modélisation de la problématique est décrite dans la section quatre.
    - :five: L'évaluation des résultats est effectuée dans la section cinq.
    
    
    ## Collecte des données
    
    Identifier, collecter et comprendre les données disponibles. Cette
    étape révèle souvent des contraintes qui obligent à revisiter le
    cadrage.  Inventorier les sources de données disponibles (BDD, APIs,
    fichiers...)  Évaluer la qualité, la volumétrie et la fraîcheur des
    données Analyse exploratoire (EDA) : distributions, corrélations,
    valeurs manquantes Détecter les biais et anomalies dans les données
    Vérifier les aspects légaux (RGPD, licences)
    
    
    
    réalisation d'une étude en data science, à savoir : projet aborde les
    différentes commence par décrire les données sur lesquels les
    algorithmes implémentés ont été entrainés et testés. Ils abordera par
    la suite les différentes étapes de prétraitements utilisées pour
    transformer les données aux formats attendus par les algorithmes
    étudiés pour la réalisation du projet. Il présentera également les
    deux approches d'apprentissage implémentés comme solutions à la
    problématique posées et justifera le choix de la solution retenue par
    l'équipe projet.
    
    ## Données
    
    ## Etapes de la réalisation
    
    ### Prétraitements
    
    
    ### Traitement
    
    #### Machine learning
    
    #### Deep learning
    
    ## Modélisation retenue
    
    
    ## Test et validation
    
    ## Conclusion

    """
)
