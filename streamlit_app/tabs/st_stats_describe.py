import streamlit as st


#Title = "st_stats_describe.py"
sidebar_name = "st_stats_describe.py"

def run():


    st.set_page_config(
        page_title="Presentation Dataset",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    #st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.title("Description du Dataset Reco Plantes",text_alignment="center")

    col1, col2, col3 = st.columns([1, 4, 1])


    with  col2:
        st.subheader("Vue d'ensemble", text_alignment="center")
        st.image("streamlit_app/assets/01_resume_global_20260323_205728.png", width="stretch")

        #st.image("streamlit_app/assets/distributionClasses.png", width=750)

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("Nombre d'images par classe",text_alignment="center")

        st.image("streamlit_app/assets/02_distri_classes_20260323_205728.png", width="stretch")

        # st.image("streamlit_app/assets/distributionClasses.png", width=750)

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("Distribution des caractéristiques des images",text_alignment="center")

        st.image("streamlit_app/assets/04_histogrammes_complets_20260323_205728.png", width="stretch")


        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("Distribution des Hauteurs/Largeurs des images",text_alignment="center")

        st.image("streamlit_app/assets/03_dimensions_20260323_205728.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("Distribution des Doublons perceptuels ", text_alignment="center")

        st.image("streamlit_app/assets/duplicate_results_20260325_210411.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.subheader("Quelques exemples d'images ", text_alignment="center")

        st.image("streamlit_app/assets/extraitImages_1.png", width="stretch")







