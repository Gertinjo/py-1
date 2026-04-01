import pandas as pd
import streamlit as st

st.header("Displaying dataframes")


data = pd.DataFrame({
    'Name': ['Gerti' , 'Dren' , 'Deon'],
    'Age': ['12' , '17' , '15'],
    'City': ['Ferizaj', 'Prizeren' , 'Klines']
})

st.dataframe(data)