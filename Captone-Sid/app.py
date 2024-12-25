import streamlit as st
import os
import numpy as np
import pandas as pd
from src.mlProject.pipeline.prediction import PredictionPipeline

st.title("Lung Cancer Prediction")

if st.button("Train Model"):
    os.system("python main.py")  # Keep training separate
    st.success("Training Complete!")

with st.form("prediction_form"):
    st.header("Enter Lung Cancer Survey Data:")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, value=30)
    smoking = st.selectbox("Smoking", [0, 1])  # 0: No, 1: Yes
    yellow_fingers = st.selectbox("Yellow Fingers", [0, 1])  # 0: No, 1: Yes
    anxiety = st.selectbox("Anxiety", [0, 1])  # 0: No, 1: Yes
    peer_pressure = st.selectbox("Peer Pressure", [0, 1])  # 0: No, 1: Yes
    chronic_disease = st.selectbox("Chronic Disease", [0, 1])  # 0: No, 1: Yes
    fatigue = st.selectbox("Fatigue", [0, 1])  # 0: No, 1: Yes
    allergy = st.selectbox("Allergy", [0, 1])  # 0: No, 1: Yes
    wheezing = st.selectbox("Wheezing", [0, 1])  # 0: No, 1: Yes
    alcohol_consuming = st.selectbox("Alcohol Consuming", [0, 1])  # 0: No, 1: Yes
    coughing = st.selectbox("Coughing", [0, 1])  # 0: No, 1: Yes
    shortness_of_breath = st.selectbox("Shortness of Breath", [0, 1])  # 0: No, 1: Yes
    swallowing_difficulty = st.selectbox("Swallowing Difficulty", [0, 1])  # 0: No, 1: Yes
    chest_pain = st.selectbox("Chest Pain", [0, 1])  # 0: No, 1: Yes

    submitted = st.form_submit_button("Predict")

    if submitted:  # Only make predictions when form submitted to avoid unnecessary calls
        try:
            data = {
                "GENDER": gender,
                "AGE": age,
                "SMOKING": smoking,
                "YELLOW_FINGERS": yellow_fingers,
                "ANXIETY": anxiety,
                "PEER_PRESSURE": peer_pressure,
                "CHRONIC DISEASE": chronic_disease,
                "FATIGUE ": fatigue,
                "ALLERGY ": allergy,
                "WHEEZING": wheezing,
                "ALCOHOL CONSUMING": alcohol_consuming,
                "COUGHING": coughing,
                "SHORTNESS OF BREATH": shortness_of_breath,
                "SWALLOWING DIFFICULTY": swallowing_difficulty,
                "CHEST PAIN": chest_pain
            }

            # Ensure input data is a list of values in the correct order for prediction
            data = pd.DataFrame([data])

            obj = PredictionPipeline()
            prediction = obj.predict(data)

            if prediction is None:
                st.error("Prediction failed. Check your model and inputs.")
            else:
                st.success(f"Lung Cancer Status: {prediction[0]}")  # Show prediction
        except Exception as e:
            st.error(f"An error occurred: {e}")
