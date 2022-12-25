import streamlit as st
from modules import MenuModules

menu_modules = MenuModules()

# navbar options liked to functionality
navbar_options = {
                "Data Upload":menu_modules.data_upload, 
                "Profiling":menu_modules.profiling, 
                "ML":menu_modules.machine_learning, 
                "Download":menu_modules.download_model}

# navbar design
with st.sidebar:
    st.image("../images/logo_automl.png")
    st.title("AutoML")
    option = st.radio("Navigation", navbar_options)
    st.info("Build an entire ML pipeline with Pandas Profiling, PyCaret, Scikit Learn and Streamlit web interface. This allows for the fast building and training of basic ML models.")

# if there is a valid choice, execute the assigned function
if option in navbar_options.keys():
    navbar_options[option]()