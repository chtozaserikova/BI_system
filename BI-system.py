import folders.prediction.prediction as prediction
import folders.analysis.analytics as analytics
import folders.home.home as home
import streamlit as st

st.sidebar.title("Welcome")
selection1 = st.sidebar.selectbox('Menu',['Home','Analytics','Prediction'])
if selection1 == 'Home':
    home.start_home() 
if selection1 == 'Analytics':
    analytics.start_analytics()        
if selection1 == 'Prediction':
    prediction.start_prediction() 




