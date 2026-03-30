import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Ce nom apparaîtra dans la sidebar du main
sidebar_name = "📊 Présentation des Modèles"

def run():
    """
    Cette fonction est appelée par main.py.
    Elle contient TOUTE la logique de votre nouvelle page avec ses propres onglets.
    """
    st.title("📈 Analyse Comparative : Modèles ML & DL")
    st.markdown("---")

    # --- VOS SOUS-ONGLETS INTERNES (Ne touchent pas au main) ---
    tab_rf, tab_rf2, tab_lr, tab_cnn, tab_vgg16, tab_res50 = st.tabs([
        "🌲 Random Forest ave SIFT",
        "🌲 Random Forest ave PCA",
        "🚀 Logistic Regression",
        "🧠 CNN",
        "🔮 VGG16",
        "🔮 Resnet50"
    ])

    #Contenu Onglet 1
    # with tab_rf:
    #     st.header("🌲 Random Forest avec SIFT")
    #     st.subheader("Résultats avec SIFT", text_alignment="center")
    #     #st.image("assets/assets/VGG16_1.png", width="stretch")
    #
    with tab_rf2:
        st.header("🌲 Random Forest avec PCA")
        st.subheader("Matrice de confusion ", text_alignment="center")
        st.image("streamlit_app/assets/matrice_confusion_random_forest.png", width="stretch")
        st.subheader("Rapport de classification", text_alignment="center")
        st.image("streamlit_app/assets/random_forest_classification_report.png", width="stretch")
    #
    # # Contenu Onglet 2
    with tab_lr:
        st.header("🚀  Logistic Regression",)
        st.subheader("Matrice de confusion ", text_alignment="center")
        st.image("streamlit_app/assets/matrice_confusion_logistic_regression.png", width="stretch")
        st.subheader("Rapport de classification", text_alignment="center")
        st.image("streamlit_app/assets/logistic_regression_classification_report.png", width="stretch")

    # # Contenu Onglet 3
    with tab_cnn:
        st.header("🧠 CNN")
        st.subheader("Accuracy ", text_alignment="center")
        st.image("streamlit_app/assets/cnn_accuracy.png", width="stretch")
        st.subheader("Loss", text_alignment="center")
        st.image("streamlit_app/assets/cnn_loss.png", width="stretch")
        st.subheader("Matrice de confusion", text_alignment="center")
        st.image("streamlit_app/assets/cnn_confusion_matrix.png", width="stretch")

    # Contenu Onglet 4
    with tab_vgg16:
        st.header("🔮 VVG16")
        st.subheader("Accuracy ", text_alignment="center")
        st.image("streamlit_app/assets/cnn_accuracy.png", width="stretch")
        st.subheader("Matrice de confusion", text_alignment="center")
        st.image("streamlit_app/assets/matrice_confusion_vgg16.png", width="stretch")

    with tab_res50:
        st.header("🔮 Resnet50")
        st.subheader("Accuracy ", text_alignment="center")
        st.image("streamlit_app/assets/resnet50_accuracy.png", width="stretch")
        st.subheader("Loss", text_alignment="center")
        st.image("streamlit_app/assets/resnet50_loss.png", width="stretch")

    # Synthèse
    # st.markdown("---")
    # st.subheader("🎯 Synthèse")
    # c1, c2, c3, c4 = st.columns(4)
    # c1.metric("Meilleur Accuracy", "93.5%", "Transformer")
    # c2.metric("Meilleur Compromis", "89.2%", "XGBoost")
    # c3.metric("Plus Rapide", "15 min", "XGBoost")
    # c4.metric("Plus Interprétable", "87.5%", "Random Forest")
