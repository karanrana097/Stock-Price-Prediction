import streamlit as st
from predict import HDFC_close

def show_explore_page():
    st.subheader("Graph showing the Variation in Stock Price over last 4 years")
    st.write("")
    st.line_chart(HDFC_close,width=600,height=480)