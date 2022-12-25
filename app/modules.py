import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
import os

class MenuModules:
    def __init__(self):
        self._df = self.check_datadir()


    def check_datadir(self):
        if os.path.exists("data/sourcedata.csv"):
            return pd.read_csv("data/sourcedata.csv", index_col=None)
        else:
            return None

    # expects a file input containing a data set
    def data_upload(self):
        st.title("Upload Data For Modelling")

        if self._df is not None:
            st.dataframe(self._df)
        else:
            file = st.file_uploader("Upload Data Set:")
            # read file and write the csv into the "data" directory
            if file:
                self._df = pd.read_csv(file, index_col=None)
                self._df.to_csv("data/sourcedata.csv", index=None)
                st.dataframe(self._df)

    def profiling(self):
        st.title("Data Profiling")
        profile_report = self._df.profile_report()
        st_profile_report(profile_report)

    def machine_learning(self):
        st.title("ML training")

    def download_model(self):
        st.title("Download Model")