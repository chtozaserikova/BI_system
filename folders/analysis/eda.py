import itertools
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind


def start_eda():
    st.title("Exploratory Data Analysis")
    st.header("Histograms")
    df = pd.read_csv("folders/dataset/diabetes.csv")
    
    #HISTOGRAMS
    #2 columns - Pregnancies and Age
    col1, col2 = st.columns(2)
    with col1:
        fig = px.histogram(df, x="Pregnancies", nbins=50, title='PREGNANCIES', labels={"Pregnancies": 'Pregnancies'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')

    with col2:
        fig = px.histogram(df, x="Age", color='Age', nbins=50, title='AGE', labels={"Age": 'Age'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
    
    #2 columns - BMI and Outcome
    col3, col4 = st.columns(2)
    with col3:
        fig = px.histogram(df, x="BMI", nbins=50, title='BMI', labels={"BMI": 'BMI'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
    with col4:
        fig = px.histogram(df, x="Outcome", color='Outcome', nbins=50, title='OUTCOME', labels={"Outcome": 'Outcome'},width=400, height=400)
        st.plotly_chart(fig, use_container_width=False, sharing='streamlit')
    
    #ORRELATION
    st.header("Correlation")
    fig, ax = plt.subplots(figsize=(10, 10))
    # pvals = df.corr(method = lambda x, y: pearsonr(x, y)[1]) - np.eye(*df.corr().shape)
    corrs = {}
    columns = df.columns.tolist()
    for col_a, col_b in itertools.combinations(columns, 2):
        corrs[col_a + '__' + col_b] = pearsonr(df.loc[:, col_a], df.loc[:, col_b])
    result = pd.DataFrame.from_dict(corrs, orient='index')
    result.columns = ['stat', 'p-value']
    pval = result['p-value'].tolist()
    psig = 0.05
    extreme = 0.95
    st.header("Матрица корреляций по Пирсону")
    sns.heatmap(df.corr(method='pearson'), annot=True, cbar = True, cmap='Blues')
    fig.tight_layout()
    st.pyplot(fig)