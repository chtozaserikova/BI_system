import streamlit as st
import folders.analysis.analysis as analysis
import folders.analysis.dataset as dataset 
import folders.analysis.eda as eda

def start_analytics():
    selection1 = st.sidebar.selectbox('',['Dataset','EDA','Analysis'])
    if selection1 == 'Dataset':
        dataset.start_dataset() 
    if selection1 == 'EDA':
        eda.start_eda()        
    if selection1 == 'Analysis':
        analysis.start_analysis() 