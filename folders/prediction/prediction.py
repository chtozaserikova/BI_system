import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
import folders.prediction.decision_tree as decision_tree
import folders.prediction.linear_regression as linear_regression
import folders.prediction.logistic_regression as logistic_regression


def start_prediction(df):
  st.title("Prediction")
  # df = pd.read_csv("folders/dataset/diabetes.csv")
  
  #ь деление выборки на тестовую и трейновую
  dataset_drop_outcome = df.drop(['Outcome'],1)
  outcome = df['Outcome']
  x_train, x_test, y_train, y_test = train_test_split(dataset_drop_outcome, outcome, test_size=0.2)


  def get_user_data():
    user_pregnancies = st.sidebar.slider("Pregnancies",0, 15, 1)
    user_glucose = st.sidebar.slider("Glucose", 0, 200, 110)
    user_blood_pressure = st.sidebar.slider("Blood pressure", 0, 122, 72)
    user_skin_thickness = st.sidebar.slider("Skin thickness", 0, 99, 20)
    user_insulin = st.sidebar.slider("Insulin", 0, 900, 30)
    user_bmi= st.sidebar.slider("BMI", 0.0, 70.0, 15.0)
    user_dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.0)
    user_age = st.sidebar.slider ("Age", 15, 100, 21)


    user_data = { 'pregnancies': user_pregnancies,
                  'glucose': user_glucose,
                  'blood_pressure': user_blood_pressure,
                  'skin_thickness': user_skin_thickness,
                  'insulin': user_insulin,
                  'bmi': user_bmi,
                  'dpf': user_dpf,
                  'age': user_age}

    features = pd.DataFrame(user_data, index=[0])
    return features


  user_input_variables = get_user_data()

  options = st.sidebar.radio('Какую модель используем?', ('Linear Regression','Decision Tree', 'Logistic Regression'))
  if options == 'Decision Tree':
    decision_tree.start_decision_tree(dataset_drop_outcome, outcome,  x_train, y_train, x_test, y_test, user_input_variables)
  elif options == 'Logistic Regression':
    logistic_regression.start_logistic(dataset_drop_outcome, outcome,  x_train, y_train, x_test, y_test, user_input_variables)
  else:
    linear_regression.start_linear(dataset_drop_outcome, outcome,  x_train, y_train, x_test, y_test, user_input_variables)