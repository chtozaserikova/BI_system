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

    # точность классификации
    st.subheader('Сдвиг: ')
    st.write(lin_model.intercept_)

    # точность классификации
    st.subheader('Коэффициент при x: ')
    st.write(lin_model.coef_)

    # точность классификации
    st.subheader('Среднеквадратичная ошибка: ')
    st.write(mean_squared_error(y_test, lin_model.predict(x_test)))


    prediction_tree=lin_model.predict(user_input_variables)
    st.subheader('Предсказание:')
    st.write(prediction_tree)
    for x in prediction_tree:
        if np.round(x) == 0:
            st.write("Negative")
        else:
            st.write("Positive")
  

# def calc(slope, intercept, hours):
#     return slope*hours+intercept

# score = calc(regressor.coef_, regressor.intercept_, 9.5)