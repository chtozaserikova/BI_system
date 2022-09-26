import pandas as pd
import streamlit as st
from help import statistic

def start_dataset():
    st.title("Dataset")
    df = pd.read_csv("folders/dataset/diabetes.csv")
    st.dataframe(df)
    rows = df.shape[0]
    columns = df.shape[1]

    st.write("There are %d rows and %d columns in the dataset."%(rows,columns))

    st.header("Statistics of dataframe")
    st.write(df.describe())

    columns = ['Асимметрия', 'Эксцесс', 'Нормальное распределение (1-да, 0-нет)', 'Нижняя граница доверительного интервала', 'Верхняя граница доверительного интервала']
    dataframe = pd.DataFrame(columns = columns)
    for col in df.columns:
        to_append = list(df[col])
        dataframe = dataframe.append(pd.DataFrame([list(statistic(to_append))], columns=columns), ignore_index=True)
    st.dataframe(dataframe.T)
    # for col in df.columns:
    #     st.write("Info about %s:"%(col))
    #     st.write(statistic(df[col]))