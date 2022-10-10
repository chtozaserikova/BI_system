import numpy as np
import streamlit as st
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

def start_decision_tree(dataset_drop_outcome, outcome, x_train,y_train,x_test,y_test,user_input_variables):

    decision_tree_model = DecisionTreeClassifier(criterion='entropy', max_depth=7, min_samples_leaf=3, random_state=2022)
    decision_tree_model.fit(x_train, y_train)

    st.header("Decision Tree Model")

    # точность классификации
    st.subheader('Точность: ')
    st.write(accuracy_score(y_test, decision_tree_model.predict(x_test))*100)

    # кросс-валидация
    st.subheader('Метод кросс-валидации: ')
    st.write(np.mean(cross_val_score(decision_tree_model,dataset_drop_outcome.values,outcome,cv=10))*100)
    
    # Матрица ошибок
    st.subheader('Матрица ошибок: ')
    st.write(confusion_matrix(y_test, decision_tree_model.predict(x_test)))
    

    prediction_tree=decision_tree_model.predict(user_input_variables)
    st.subheader('Предсказание:')
    st.write(prediction_tree)
    if prediction_tree == 0:
        st.write("Negative")
    else:
        st.write("Positive")
  