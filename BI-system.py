import folders.prediction.prediction as prediction
import folders.analysis.analytics as analytics
import folders.home.home as home
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="BI system",
    page_icon="🕸",
    layout="wide",
    initial_sidebar_state="expanded")

 # Setup file upload
uploaded_file = st.sidebar.file_uploader(
                        label="Загрузите CSV или Excel файл. (200MB max)",
                        type=['csv', 'xlsx']) 
global df 
if uploaded_file is not None:
    print(uploaded_file)
    print("Ok")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        # print(e)
        df = pd.read_excel(uploaded_file)

st.sidebar.title("Welcome")
selection1 = st.sidebar.selectbox('Menu',['Home','Analytics','Prediction'])
if selection1 == 'Home':
    home.start_home() 
if selection1 == 'Analytics':
    analytics.start_analytics(df)        
if selection1 == 'Prediction':
    prediction.start_prediction(df) 