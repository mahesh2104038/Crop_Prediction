import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import numpy as np

st.write(f"## Crop Prediction Application")
st.write("Author: Mahesh Kurhe")

Crop_prediction_model = pickle.load(open(r"Crop_prediction.sav", "rb"))
with st.sidebar:
    selected = option_menu("Crop Prediction", ["Crop prediction"])

if selected == "Crop prediction":
    st.write("Welcome to Crop predection Appilcation")
    st.write("Please input details of your soil")

    N = st.text_input("Type your N value")
    P = st.text_input("Type your P value")
    K = st.text_input("Type your K value")
    temperature = st.text_input("Type your temperature value")
    humidity = st.text_input("Type your humidity value")
    ph = st.text_input("Type your ph value")
    rainfall = st.text_input("Type the Rainfall value")
if st.button("Predict"):
        data = [N, P, K, temperature, humidity, ph, rainfall]
        data_array = np.array(data, dtype=float).reshape(1,-1)
        prediction = Crop_prediction_model.predict(data_array)
        st.write(f"## Prediction: {prediction}")
