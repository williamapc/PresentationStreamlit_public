import streamlit as st
import tensorflow as tf
from PIL import Image  # Pour manipuler les images
import numpy as np
import os  # Pour vérifier l'existence du fichier modèle


def run():
    st.set_page_config(
        page_title="Inférence",
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="expanded",
    )




    st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif", width=1600)

    IMG_HEIGHT = 224
    IMG_WIDTH = 224


    classes_names = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                     'Black-grass___healthy',
                     'Blueberry___healthy', 'Charlock___healthy', 'Cherry_(including_sour)___healthy',
                     'Cherry_(including_sour)___Powdery_mildew', 'Cleavers___healthy', 'Common Chickweed___healthy',
                     'Common wheat___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                     'Corn_(maize)___Common_rust', 'Corn_(maize)___healthy', 'Corn_(maize)___Northern_Leaf_Blight',
                     'Fat Hen___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___healthy',
                     'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Loose Silky-bent___healthy', 'Maize___healthy',
                     'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
                     'Pepper_bell___Bacterial_spot', 'Pepper_bell___healthy', 'Potato___Early_blight', 'Potato___healthy',
                     'Potato___Late_blight', 'Raspberry___healthy', 'Scentless Mayweed____healthy',
                     'Shepherd’s Purse____healthy',
                     'Small-flowered Cranesbill____healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
                     'Strawberry___healthy',
                     'Strawberry___Leaf_scorch', 'Sugar beet___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight',
                     'Tomato___healthy', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
                     'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
                     'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus']

    # Pour cette démo, utilisons une liste factice si label_encoder n'est pas défini
    try:
        # class_names = label_encoder.classes_
        classes_names
        class_names = [f'Class_{i}' for i in range(50)]
        # st.write(class_names)
    except NameError:
        st.warning("label_encoder not found. Using a dummy list of class names.")
        # Vous DEVEZ remplacer ceci par vos vrais noms de classes en production
        class_names = [f'Class_{i}' for i in range(50)]
        # st.write(class_names)  # Exemple avec 50 classes
        # class_names = classes_names
    # --- Configuration de l'application Streamlit ---
    st.title("Application de Classification des Maladies des Plantes")
    st.write("Téléchargez une image pour identification de l'espèce et éventuellement de la maladie.")


    # --- Chargement du modèle (mise en cache pour l'efficacité) ---
    # Utilisez le décorateur @st.cache_resource pour charger le modèle une seule fois
    @st.cache_resource
    def load_trained_model(model_path):
        """Charge le modèle TensorFlow/Keras entraîné."""
        if not os.path.exists(model_path):
            st.error(f"Fichier modèle introuvable : {model_path}")
            st.stop()  # Arrête l'exécution si le fichier n'est pas là
        try:
            model = tf.keras.models.load_model(model_path)
            st.success("Modèle chargé avec succès !")
            return model
        except Exception as e:
            st.error(f"Erreur lors du chargement du modèle : {e}")
            st.stop()


    # Spécifiez le chemin vers votre fichier modèle sauvegardé
    model_path = 'notebooks/reco_plantes_vgg16.keras'  # Assurez-vous que ce fichier est accessible

    model = load_trained_model(model_path)


    # --- Fonction de prétraitement de l'image ---
    def preprocess_image(image):
        """Prétraite l'image pour qu'elle corresponde au format d'entrée du modèle."""
        img = image.resize((IMG_WIDTH, IMG_HEIGHT))  # Redimensionnement
        img_array = np.array(img)  # Convertir en tableau NumPy
        # Appliquer la même normalisation que pendant l'entraînement (si applicable)
        # Pour MobileNetV2 entraîné sur ImageNet, l'entrée attend souvent des valeurs entre 0 et 1
        img_array = img_array / 255.0  # Normalisation si le modèle attend [0, 1]
        # Ajouter une dimension de lot (le modèle attend un lot d'images)
        img_array = np.expand_dims(img_array, axis=0)
        return img_array


    # --- Interface utilisateur pour le téléchargement d'image ---
    uploaded_file = st.file_uploader("Choisissez une image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Afficher l'image téléchargée
        image = Image.open(uploaded_file)
        st.image(image, caption="Image téléchargée.", width="content")
        # st.write(type(image))

        # Prétraiter l'image
        processed_image = preprocess_image(image)
        # st.write(type(processed_image.shape))
        st.write(processed_image.shape)
        # Faire la prédiction
        if model:  # S'assurer que le modèle a été chargé
            st.write("Classification en cours...")
            predictions = model.predict(processed_image)
            st.write(predictions)
            st.text(f'predictions.shape : {predictions.shape}')
            # Obtenir l'indice de la classe avec la probabilité la plus élevée
            predicted_class_index = np.argmax(predictions, axis=1)[0]
            # predicted_class_index = predicted_class_index.item()
            # st.write(predicted_class_index)
            # predicted_class_index = predicted_class_index.item()
            # predicted_class_index = np.argmax(predictions, axis=1).item()
            st.write(f"Classe : {class_names[predicted_class_index]}")
            # predicted_class_index = np.argmax(predictions)
            # predicted_class_index = int(predicted_class_index[0])
            # predicted_class_index = predicted_class_index.item()
            # Obtenir la probabilité associée
            confidence = np.max(predictions)

            # Obtenir le nom de la classe prédite
            # if 0 <= predicted_class_index < len(class_names):
            #     predicted_class_name = class_names[predicted_class_index]
            if 0 <= predicted_class_index < len(classes_names):
                predicted_class_name = class_names[predicted_class_index]
            else:
                predicted_class_name = "Classe inconnue"  # Gérer les cas inattendus

            # Afficher le résultat
            st.write("---")
            st.subheader("Résultat de la Classification :")
            st.write(f"Prédiction : **{predicted_class_name}**")
            # st.write(f"Confiance : **{confidence:.2f}**")
            st.write(f"Confiance : {confidence}")

            # Optionnel : Afficher les probabilités pour toutes les classes
            st.write("Probabilités par classe :")
            prob_dict = {class_names[i]: float(predictions[0][i]) for i in range(len(class_names))}
            st.json(prob_dict)

    else:
        st.write("Veuillez télécharger une image pour commencer la classification.")
