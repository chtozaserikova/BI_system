from PIL import Image
import streamlit as st
import pandas as pd

def start_home():
    st.title("BI Analytics & Prediction System")
    st.subheader("""Это система бизнес-аналитики, которая предоставляет всю информацию для исследования числовых наборов данных. У вас в руках будут все опции аналитики и прогнозирования. Наслаждайтесь!""")
    image = Image.open('folders/home/img_new.jpg')
    st.image(image, caption='')
