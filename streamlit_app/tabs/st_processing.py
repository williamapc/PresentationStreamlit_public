import streamlit as st
from pathlib import Path
import pandas as pd


# sidebar_name = "st_prepro.py"

def run():

    st.set_page_config(
        page_title="Procesing",
        page_icon="⛳",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/3.gif", width=1600)

    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 4, 1])

    with  col2:
        st.title("Eléments du processing",text_alignment="center")

        # st.subheader("Random Forest learning type")
        #
        # file_path = Path(__file__).parent / "" / "processing_RForest.txt"
        # #print(file_path)
        # with file_path.open(encoding="utf-8") as f:
        #     text = f.read()
        #
        # st.text(text)
        # # st.text_area("")
        #
        # st.divider()
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.title("VGG16", text_alignment="center")
        st.subheader("VGG16 avant dégel",text_alignment="center")
        st.image("streamlit_app/assets/VGG16_1.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("VGG16 après dégel",text_alignment="center")
        st.image("streamlit_app/assets/VGG16_2.png", width="stretch")
