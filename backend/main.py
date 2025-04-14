from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BMIRequest(BaseModel):
    height_cm: float
    weight_kg: float

@app.post("/bmi")
def calculate_bmi(data: BMIRequest):
    height_m = data.height_cm / 100
    bmi = data.weight_kg / (height_m ** 2)
    category = (
        "Underweight" if bmi < 18.5 else
        "Normal weight" if bmi < 24.9 else
        "Overweight" if bmi < 29.9 else
        "Obese"
    )
    return {"bmi": round(bmi, 2), "category": category}