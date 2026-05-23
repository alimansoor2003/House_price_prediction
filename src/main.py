from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
from src.config import MODEL_PATH # ✔ import from config

app = FastAPI()

model = pickle.load(open(MODEL_PATH, "rb"))

# ----------------------------
# Pydantic schema (IMPORTANT)
# ----------------------------
class HouseInput(BaseModel):
    Area: float
    Bedrooms: int
    Bathrooms: int
    Floors: int
    YearBuilt: int
    Condition: str
    Garage: str
    Location: str

# ----------------------------
# Prediction endpoint
# ----------------------------
@app.post("/predict")
def predict(data: HouseInput):

    input_dict = {
        "Area": data.Area,
        "Bedrooms": data.Bedrooms,
        "Bathrooms": data.Bathrooms,
        "Floors": data.Floors,
        "YearBuilt": data.YearBuilt,
        "Condition": data.Condition,
        "Garage": data.Garage,
        "Location": data.Location
    }

    features = pd.DataFrame([input_dict])

    prediction = model.predict(features)[0]

    return {
        "predicted_price": float(prediction)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)