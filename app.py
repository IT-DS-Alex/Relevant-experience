# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:47:48 2023

@author: mixal
"""
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import plotly.express as px


st.title('StreamLit example')
st.header('Samples from dataset: test')

dat = pd.read_csv('train.csv')
years = np.unique(dat.year)
brand = np.unique(dat.make.astype('str'))
model = np.unique(dat.model.astype('str'))


st.sidebar.markdown("## Load Data to Get Forecast")
select_event_2 = st.sidebar.selectbox(
    'What brand car are you selling?', brand.tolist())


st.header('Dataset statistics: ' + str(select_event_2))
datX = dat[dat.make == select_event_2]
datX = datX.dropna()
st.write(datX.describe())

fig, ax = plt.subplots()
ax = sns.scatterplot(data = datX, x="year", y="sellingprice")
st.header('Scatter Plot Chart Cost and Year')
st.pyplot(fig)


fig = px.scatter(
    datX,
    x="year",
    y="sellingprice",
    size="condition",
    color="model",
    hover_name="seller",
    log_x=True,
    size_max=60,
)


tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])

with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)

select_event = st.sidebar.selectbox('What year car are you selling?', years.tolist())
# select_event_2 = st.sidebar.selectbox(
#     'What brand car are you selling?', brand.tolist())
    
with st.sidebar:
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

# predict = model.predict(bytes_data)
# st.header('This subtitles is so english level: ', predict)
    

with st.sidebar:
    st.button('Want FORECAST')
