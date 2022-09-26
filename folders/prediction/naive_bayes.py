import numpy as np
import streamlit as st
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix 

def start_naive_bayes(dataset_drop_outcome, outcome,  x_train, y_train, x_test, y_test, user_input_variables):
    #Model training
    gnb = GaussianNB()
    gnb.fit(x_train, y_train)

    st.header("Naive Bayes Model")
    
    #Model accuracy
    st.subheader('Model test accuracy: ')
    st.write(accuracy_score(y_test,gnb.predict(x_test))*100)

    #Model Cross Validation
    st.subheader('Model Cross Validation: ')
    st.write(np.mean(cross_val_score(gnb, dataset_drop_outcome.values,outcome,cv=10))*100)

    #Model Confusion Matrix
    st.subheader('Confusion Matrix: ')
    st.write(confusion_matrix(y_test, gnb.predict(x_test)))

    #Model prediction
    prediction_naive=gnb.predict(user_input_variables)
    st.subheader('Prediction:')
    st.write(prediction_naive)
    if prediction_naive == 0:
        st.write("Negative")
    else:
        st.write("Positive")