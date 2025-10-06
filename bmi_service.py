from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()

class BMIRequest(BaseModel):
    weight: float  # in kilograms
    height: float  # in meters

class BMIResponse(BaseModel):
    bmi: float
    category: str

def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

@app.post("/bmi", response_model=BMIResponse)
def calculate_bmi(data: BMIRequest):
    bmi = data.weight / (data.height ** 2)
    category = bmi_category(bmi)
    return BMIResponse(bmi=round(bmi, 2), category=category)