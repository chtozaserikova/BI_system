import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

def start_analysis():
  st.title("Analysis")
  df = pd.read_csv("folders/dataset/diabetes.csv")
  
  #bar chart
  bar_fig = px.bar(df, x="Age", y="Pregnancies", color='Age', title="AGE X PREGNANCIES",width=800, height=440)
  st.plotly_chart(bar_fig, use_container_width=False, sharing='streamlit')
  
  #pie chart
  pie_fig = px.pie(df, values ='Pregnancies', names='Pregnancies', title='AMOUNT OF PREGNANCIES')
  st.plotly_chart(pie_fig)

  #area chart
  area_fig = px.area(df, x="Age", y="BMI", title="AGE X BMI",width=800, height=440)
  st.plotly_chart(area_fig, use_container_width=False, sharing='streamlit')

  #scatter chart
  scatter_fig = go.Scatter(x = df['BMI'], y = df['Insulin'], mode = 'markers')
  scatter_data = [scatter_fig]
  

  scatter_layout = go.Layout(title='BMI X INSULIN',
                   yaxis={'title':'Insulin'},
                   xaxis={'title': 'BMI'},width=800, height=440)
  scatter_Fig = go.Figure(data=scatter_data, layout=scatter_layout)
  st.plotly_chart(scatter_Fig)
  
  #box chart
  box_trace1 = go.Box(y = df.loc[df['Outcome'] == 1, 'Age'], 
                name = 'Tested positive',
                marker = {'color': 'green'})
  
  box_trace2 = go.Box(y = df.loc[df['Outcome'] == 0, 'Age'],
                name = 'Tested negative',
                marker = {'color': 'red'})
  box_layout = go.Layout(title="TESTED POSITIVE AND NEGATIVE PER AGE (DISPERSION)",
                          yaxis={'title': 'Age'},
                          xaxis={'title': 'Test status'},width=870, height=440)
  box_data = [box_trace1,box_trace2]
  box_Fig = go.Figure(data=box_data,layout=box_layout)
  st.plotly_chart(box_Fig)

  