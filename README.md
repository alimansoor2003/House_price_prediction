**🏠 House Price Prediction API **
A Machine Learning project that predicts 
house prices using a trained regression 
model and exposes it through a FastAPI backend. 
The system is deployed and ready for real-world usage
via a cloud API.

**🚀 Live API**
  👉 https://house-price-prediction-api-6q6e.onrender.com/
  👉 Swagger Docs: /docs
  
**📌 Project Overview**
This project builds an end-to-end ML pipeline:
-Data preprocessing
-Feature engineering
-Model training
-Model serialization
-FastAPI deployment
-Cloud hosting (Render)
The model predicts house prices based on features like area, bedrooms, bathrooms, floors, location, etc.

**🧠 Machine Learning Approach**
-Algorithm: Linear Regression
-Feature Engineering:
  One-Hot Encoding for Location
  Binary encoding for Garage
  Custom feature: Family indicator
  Normalization of target price
**⚙️ Tech Stack**
-Python 🐍
-Pandas & NumPy
-Scikit-learn
-FastAPI
-Uvicorn
-Pickle (model serialization)
-Render (deployment)

**How to Run Locally**
1. Clone repo
git clone https://github.com/your-username/House_price_prediction.git
cd House_price_prediction
2. Create environment
pip install -r requirements.txt
3. Run FastAPI
uvicorn src.main:app --reload

**📈 Future Improvements**
-Replace Linear Regression with XGBoost / Random Forest
-Add proper data validation (Pydantic models)
-Add CI/CD pipeline
-Dockerize application
-Add frontend UI (React or Streamlit)



