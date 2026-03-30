import streamlit as st

# Title = "st_stats_describe.py"
sidebar_name = "st_interpretability.py"


def run():
    st.set_page_config(
        page_title="Interpretability",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # st.image("https://dst-studio-template.s3.eu-west-3.amazonaws.com/2.gif")
    st.markdown("<br><br>", unsafe_allow_html=True)

    st.title("Interpretabilité avec Grad-CAM", text_alignment="center")

    col1, col2, col3 = st.columns([1, 4, 1])

    with  col2:
        st.subheader("Exemple de carte de chaleur sur 1 image bien discriminée", text_alignment="center")
        st.image("streamlit_app/assets/conv2D_first_layer_fig1.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        #st.subheader("Exemple de carte de chaleur sur la deuxième couche de Convolution", text_alignment="center")
        st.image("streamlit_app/assets/conv2D_second_layer_fig2.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        #st.subheader("Exemple de carte de chaleur sur la troisième couche de Convolution", text_alignment="center")
        st.image("streamlit_app/assets/conv2D_third_layer_fig3.png", width="stretch")

        st.subheader("Exemple de carte de chaleur sur 1 image floue", text_alignment="center")
        st.image("streamlit_app/assets/conv2D_first_layer_fig6.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)
        st.image("streamlit_app/assets/conv2D_third_layer_fig4.png", width="stretch")



        #st.subheader("Exemple de carte de chaleur sur la deuxième couche de Convolution", text_alignment="center")
        st.image("streamlit_app/assets/conv2D_second_layer_fig5.png", width="stretch")

        st.markdown("<br><br>", unsafe_allow_html=True)

        #st.subheader("Exemple de carte de chaleur sur la troisième couche de Convolution", text_alignment="center")


