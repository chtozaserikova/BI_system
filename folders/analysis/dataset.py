import pandas as pd
import streamlit as st
from help import statistic

def start_dataset(df):
    st.title("Dataset")
    # df = pd.read_csv("folders/dataset/diabetes.csv")
    st.dataframe(df)
    rows = df.shape[0]
    columns = df.shape[1]

    st.write("В данном наборе данных %d строк и %d столбцов (признаков)"%(rows,columns))

    st.header("Статистика")
    st.write(df.describe())

    columns = ['Асимметрия', 'Эксцесс', 'Нормальное распределение (1-да, 0-нет)', 'Нижняя граница доверительного интервала', 'Верхняя граница доверительного интервала']
    dataframe = pd.DataFrame(columns = columns)
    for col in df.columns:
        to_append = list(df[col])
        dataframe = dataframe.append(pd.DataFrame([list(statistic(to_append))], columns=columns), ignore_index=True)
    st.dataframe(dataframe.T)