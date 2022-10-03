from PIL import Image
import streamlit as st

def start_home():
    st.title("BI Analytics & Prediction System")
    st.write("Это система бизнес-аналитики, которая предоставляет всю информацию для принятия решений.") 
    st.write("У вас в руках будут все опции аналитики и прогнозирования. Наслаждайтесь!")
    image = Image.open('folders/home/img_new.jpg')
    st.image(image, caption='')
    
      