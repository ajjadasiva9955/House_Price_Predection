# 🏠 House Price Prediction App : https://winequalitypredection9955.streamlit.app/

A machine learning web application built with **Streamlit** that predicts house prices based on various features such as area, number of bedrooms, bathrooms, stories, and amenities.

---

## 🚀 Features
- Predicts house prices using a trained **Linear Regression model**.
- Simple and interactive **Streamlit UI**.
- Takes inputs such as:
  - Area (sq. ft.)
  - Bedrooms
  - Bathrooms
  - Stories
  - Parking spaces
  - Main road access
  - Guestroom availability
  - Basement
  - Hot water heating
  - Air conditioning
  - Preferred area

---

## 🛠️ Tech Stack
- **Python 3**
- **Pandas**, **Scikit-learn**
- **Streamlit** for deployment
- **Pickle** for model persistence

---

## 📂 Project Structure
├── app.py # Streamlit app
├── linear_regression_model.pkl # Trained ML model
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── House price prediction.ipynb# Jupyter Notebook (training)

yaml
Copy code

---

## ⚡ Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/house-price-prediction.git
   cd house-price-prediction
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app

bash
Copy code
streamlit run app.py
Open the local URL shown in the terminal (usually http://localhost:8501/).

🧑‍💻 Training the Model
If you want to retrain the model:

Open the House price prediction.ipynb notebook.

Train models (Linear Regression, XGBoost, AdaBoost, etc.).

Save the chosen model:

python
Copy code
import pickle
with open("linear_regression_model.pkl", "wb") as f:
    pickle.dump(lin_model, f)
📊 Example Prediction
Input: Area = 3000 sq. ft., Bedrooms = 3, Bathrooms = 2, Stories = 2, Parking = 1, AC = Yes

Output: 🏡 Estimated House Price: ₹ 45,20,000
