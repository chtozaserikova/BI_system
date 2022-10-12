from PIL import Image
import streamlit as st
import pandas as pd

def start_home():
    st.title("BI Analytics & Prediction System")
    st.write("""Это система бизнес-аналитики, которая предоставляет всю информацию для исследования числовых наборов данных. У вас в руках будут все опции аналитики и прогнозирования. Наслаждайтесь!""")
    image = Image.open('folders/home/img_new.jpg')
    st.image(image, caption='')


    # # Setup file upload
    # uploaded_file = st.sidebar.file_uploader(
    #                         label="Загрузите CSV или Excel файл. (200MB max)",
    #                         type=['csv', 'xlsx']) 
    # global df 
    # if uploaded_file is not None:
    #     print(uploaded_file)
    #     print("Ok")
    #     try:
    #         df = pd.read_csv(uploaded_file)
    #     except Exception as e:
    #         print(e)
    #         df = pd.read_excel(uploaded_file)