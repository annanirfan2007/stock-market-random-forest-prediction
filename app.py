import streamlit as st
import pandas as pd
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

if not os.path.exists(MODEL_PATH):
st.error("Model file not found. Upload random_forest_model.pkl to GitHub.")
st.stop()

try:
model_data = load_model()

```
model = model_data["model"]
features = model_data["features"]
target = model_data["target"]

st.success("Random Forest Model Loaded Successfully!")
st.subheader("Enter Feature Values")
st.write(f"Prediction target: {target}")

input_values = {}

with st.form("prediction_form"):
    cols = st.columns(2)

    for i, feature in enumerate(features):
        with cols[i % 2]:
            input_values[feature] = st.number_input(
                label=feature,
                value=0.0,
                format="%.6f",
                key=feature
            )

    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame([input_values], columns=features)
    prediction = model.predict(input_df)[0]

    st.subheader("Prediction Result")
    st.metric(
        label=f"Predicted {target}",
        value=f"{prediction:,.4f}"
    )

    st.info(
        "This is a machine learning estimate, "
        "not a guaranteed future stock price."
    )
```

except Exception as e:
st.error(f"Error loading or running model: {e}")
