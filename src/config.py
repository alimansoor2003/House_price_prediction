# src/config.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
DATA_PATH = os.path.join(BASE_DIR, "data", "House Price Prediction Dataset.csv")



TEST_SIZE = 0.2
RANDOM_STATE = 42


FEATURES = [
    "Area",
    "Bedrooms",
    "Bathrooms",
    "Floors",
    "YearBuilt",
    "Condition",
    "Garage",
    "Family",
    "Location_Rural",
    "Location_Suburban",
    "Location_Urban"
]