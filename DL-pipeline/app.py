import streamlit as st
import os
import numpy as np
from src.dlProject.components.prediction import PredictionPipeline

st.title("Image Classification: Healthy vs. Coccidiosis")

# Train Model
if st.button("Train Model"):
    os.system("python main.py")  # Trigger training by running your pipeline
    st.success("Model training completed!")

# Image Classification
st.header("Upload an Image for Classification")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Classify Image"):
        try:
            # Save the uploaded file temporarily
            temp_image_path = "temp_uploaded_image.jpg"
            with open(temp_image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Perform prediction
            predictor = PredictionPipeline()
            prediction = predictor.predict(temp_image_path)

            # Process prediction output
            class_labels = ["Healthy", "Coccidiosis"]
            predicted_class = class_labels[np.argmax(prediction)]
            confidence = np.max(prediction) * 100

            st.success(f"Prediction: {predicted_class} (Confidence: {confidence:.2f}%)")
            
            # Clean up temporary file
            os.remove(temp_image_path)

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
