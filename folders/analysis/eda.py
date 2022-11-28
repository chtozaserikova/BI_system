import itertools
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from scipy.stats import pearsonr, ttest_ind
from scipy import stats
import pandas_profiling
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def start_eda(df):
    st.title("Exploratory Data Analysis")
    df = df[~df.isnull().any(axis=1)]
    df = df.select_dtypes(include='number')
    df = df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
    
    st.subheader("Матрица корреляций по Пирсону")
    st.markdown('Перед построением матрицы корреляции необходимо удалить аномалии из набора данных при помощи метода сигм.')
    st.markdown('Если значение p-value < 0.05, то существует статистически значимая связь между этими двумя переменными. Пары с незначимой связью удалены из таблицы.')
    fig, ax = plt.subplots(figsize=(10, 10))
    corrs = {}
    columns = df.columns.tolist()
    for col_a, col_b in itertools.combinations(columns, 2):
        corrs[col_a + '__' + col_b] = pearsonr(df.loc[:, col_a], df.loc[:, col_b])
    result = pd.DataFrame.from_dict(corrs, orient='index')
    result.columns = ['stat', 'p-value']
    res = result[result['p-value'] < 0.05] # если значение p < 0,05, мы приходим к выводу, что существует статистически значимая связь между этими двумя переменными.
    st.dataframe(res)
    # pval = result['p-value'].tolist()
    # psig = 0.05
    # extreme = 0.95
    # sns.heatmap(df.corr(method='pearson'), annot=True, cbar = True, cmap='Blues')
    # fig.tight_layout()
    # st.pyplot(fig)

    # создаём отчёт в HTML формате
    st.subheader("Первичный анализ данных с созданием отчета в HTML формате")
    profile = ProfileReport(df, title="Первичный анализ данных", explorative=True)
    st_profile_report(profile)
    p = profile.to_html()

    st.download_button(
        label="Скачать HTML файл",
        file_name="your_report.html",
        data=p,
    )