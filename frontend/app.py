import streamlit as st
import requests

# Function to call FastAPI endpoint
def get_bmi(height, weight):
    response = requests.post("http://localhost:8000/bmi", json={
        "height_cm": height,
        "weight_kg": weight
    })
    return response.json()

# Streamlit UI
st.title("BMI Calculator")

height = st.number_input("Height (in cm)", min_value=0.0)
weight = st.number_input("Weight (in kg)", min_value=0.0)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        result = get_bmi(height, weight)
        st.write(f"BMI: {result['bmi']} - {result['category']}")
    else:
        st.write("Please enter valid height and weight.")