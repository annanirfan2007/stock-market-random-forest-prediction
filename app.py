import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

st.set_page_config(
page_title="Stock Market Prediction",
page_icon="📈",
layout="wide"
)

st.title("📈 Stock Market Prediction")
st.write("Random Forest Machine Learning Model")

MODEL_PATH = "random_forest_model.pkl"

@st.cache_resource
def load_model():
return joblib.load(MODEL_PATH)

i

