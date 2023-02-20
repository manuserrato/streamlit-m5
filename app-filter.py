import streamlit as st
import pandas as pd

st.title("streamlit - Filter by sex")

DATA_URL = "dataset.csv"

#funcion data para lista
@st.cache
def load_data():
    data = pd.read_csv(DATA_URL)

    return data

#funcion para filtrar la lista en base de generos
@st.cache
def load_data_bysex(sex):
    data = pd.read_csv(DATA_URL)
    filtered_data_bysex = data[data("sex") == sex]

    return filtered_data_bysex

#al inicio del programa se llama la funcion load_data_

data = load_data()
selected_sex = st.selectbox("Select sex", data["sex"].unique() )
btnFilterbysex = st.button("Filter by sex")

if(btnFilterbysex):
    filterbysex = load_data_bysex(selected_sex)
    count_row = filterbysex.shape[0]
    st.write(f"Total items: {count_row}")

    st.dataframe(filterbysex)