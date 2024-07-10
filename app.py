from predict import show_predict_page
import numpy as np
import pandas as pd
import streamlit as st
from explore import show_explore_page

page = st.sidebar.selectbox("Explore or Predict",("Predict","Explore"))
if (page=="Predict"):
    show_predict_page()
else:
    show_explore_page()

