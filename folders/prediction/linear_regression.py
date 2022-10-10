import numpy as np
import streamlit as st
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def start_linear(dataset_drop_outcome, outcome, x_train,y_train,x_test,y_test,user_input_variables):

    lin_model = LinearRegression(normalize=True)
    lin_model.fit(x_train, y_train)

    st.header("Linear Regression")

    # свободный член
    st.subheader('Сдвиг: ')
    st.write(lin_model.intercept_)

    # k независимых переменных
    st.subheader('Коэффициент при x: ')
    st.write(lin_model.coef_)

    # точность классификации
    st.subheader('Средняя абсолютная ошибка: ')
    st.write(mean_absolute_error(y_test, lin_model.predict(x_test)))


    prediction_tree=lin_model.predict(user_input_variables)
    st.subheader('Предсказание:')
    st.write(prediction_tree)
    for x in prediction_tree:
        if np.round(x) == 0:
            st.write("Negative")
        else:
            st.write("Positive")