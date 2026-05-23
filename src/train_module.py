import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from src.config import MODEL_PATH,DATA_PATH
# Load data
data = pd.read_csv(DATA_PATH, index_col=0)

# ----------------------------
# Split features/target
# ----------------------------
X = data.drop("Price", axis=1)
y = data["Price"]

# ----------------------------
# Define column types
# ----------------------------
numeric_features = ["Area", "Bedrooms", "Bathrooms", "Floors", "YearBuilt"]
categorical_features = ["Location", "Garage", "Condition"]

# ----------------------------
# Preprocessing
# ----------------------------
numeric_transformer = StandardScaler()

categorical_transformer = OneHotEncoder(handle_unknown="ignore")

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# ----------------------------
# Full pipeline
# ----------------------------
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open(MODEL_PATH, "wb"))

print("✅ Production model trained and saved")