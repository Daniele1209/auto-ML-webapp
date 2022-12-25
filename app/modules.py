import streamlit as st
import pandas as pd

# expects a file input containing a data set
def data_upload():
    st.title("Upload Data For Modelling")
    file = st.file_uploader("Upload Data Set:")
    if file:
        df = pd.read_csv(file)
        st.dataframe(df)


def profiling():
    pass

def machine_learning():
    pass

def download_model():
    pass