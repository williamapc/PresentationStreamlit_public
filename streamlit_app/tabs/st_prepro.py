import streamlit as st
from pathlib import Path
import pandas as pd

# Title = "st_stats_describe.py"
# sidebar_name = "st_prepro.py"

def run():

    st.set_page_config(
        page_title="Preprocessing",
        #page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    col1, col2, col3 = st.columns([1, 4, 1])

    with  col2:
        #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif", width="stretch")
        st.markdown("<br><br>", unsafe_allow_html=True)

        st.title("Eléments du preprocessing",text_alignment="center")

        # file_path = Path(__file__).parent / "" / "prepro1.txt"
        # #st.write(file_path)
        # #file_path = "streamlit_app/prepro1.txt"
        #
        # with file_path.open(encoding="utf-8") as f:
        #     text = f.read()
        #
        # st.text(text)

        st.subheader("Extrait de Features avec SIFT et HOG",text_alignment="center")

        st.image("streamlit_app/assets/sift_hog_M_0152_copy_flipLR.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)


        st.subheader("Extrait de Features avec SIFT et HOG",text_alignment="center")

        st.image("streamlit_app/assets/sift_hog_5.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("Distribution des features extraites par SIFT et HOG",text_alignment="center")

        st.image("streamlit_app/assets/keypoints_distribution.png", width="stretch")




