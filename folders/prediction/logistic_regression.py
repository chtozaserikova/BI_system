import numpy as np
import streamlit as st
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def start_logistic(dataset_drop_outcome, outcome, x_train,y_train,x_test,y_test,user_input_variables):

    log_model = LogisticRegression()
    log_model.fit(x_train, y_train)

    st.header("Linear Regression")

    # точность классификации
    st.subheader('Сдвиг: ')
    st.write(log_model.intercept_)

    # точность классификации
    st.subheader('Коэффициент при x: ')
    st.write(log_model.coef_)

    # точность классификации
    st.subheader('Точность: ')
    st.write(accuracy_score(y_test, log_model.predict(x_test))*100)

    # кросс-валидация
    st.subheader('Метод кросс-валидации: ')
    st.write(np.mean(cross_val_score(log_model,dataset_drop_outcome.values,outcome,cv=10))*100)
    
    # Матрица ошибок
    st.subheader('Матрица ошибок: ')
    st.write(confusion_matrix(y_test, log_model.predict(x_test)))


    prediction_tree=log_model.predict(user_input_variables)
    st.subheader('Предсказание:')
    st.write(prediction_tree)
    for x in prediction_tree:
        if x == 0:
            st.write("Negative")
        else:
            st.write("Positive")