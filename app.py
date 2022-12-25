import streamlit as st

navbar_options = ["Data Upload", "Profiling", "ML", "Download"]

with st.sidebar:
    st.image("images/logo_automl.png")
    st.title("AutoML")
    option = st.radio("Navigation", navbar_options)