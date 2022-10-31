import itertools
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind
import pandas_profiling
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def start_eda(df):
    st.title("Exploratory Data Analysis")
    df = df[~df.isnull().any(axis=1)]
    df = df.select_dtypes(include='number')
    
    #CORRELATION
    st.header("Матрица корреляций по Пирсону")
    fig, ax = plt.subplots(figsize=(10, 10))
    corrs = {}
    columns = df.columns.tolist()
    for col_a, col_b in itertools.combinations(columns, 2):
        corrs[col_a + '__' + col_b] = pearsonr(df.loc[:, col_a], df.loc[:, col_b])
    result = pd.DataFrame.from_dict(corrs, orient='index')
    result.columns = ['stat', 'p-value']
    pval = result['p-value'].tolist()
    psig = 0.05
    extreme = 0.95
    sns.heatmap(df.corr(method='pearson'), annot=True, cbar = True, cmap='Blues')
    fig.tight_layout()
    st.pyplot(fig)

    # создаём отчёт в HTML формате
    profile = ProfileReport(df, title="Первичный анализ данных", explorative=True)
    st_profile_report(profile)
    p = profile.to_html()

    st.download_button(
        label="Скачать HTML файл",
        file_name="your_report.html",
        data=p,
    )