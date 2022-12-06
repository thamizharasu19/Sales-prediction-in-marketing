# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 18:32:38 2022

@author: tamil
"""

import streamlit as st
#from utils import PrepProcessor , columns

import numpy as np
import pandas as pd

import joblib

model = joblib.load('model_joblib')
st.title('PREDICT THE SALES 📈📊')
tv = st.number_input('ENTER THE VALUE OF TV')
rd = st.number_input('ENTER THE VALUE OF RADIO')
news = st.number_input('ENTER THE VALUE OF NEWSPAPER')


def predict_sales():
    rows = np.array([tv,rd,news])
    X = pd.DataFrame([rows])
    prediction = model.predict(X)[0]
    st.success('YOUR PREDICTED SALES IS : %d lakhs ' %(prediction[0]))

    #st.success('YOUR PREDICTED SALES IS : ' , prediction)

st.button('PREDICT',on_click = predict_sales)