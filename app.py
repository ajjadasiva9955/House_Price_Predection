import streamlit as st
import pandas as pd
import pickle

# ------------------------------
# Load the trained model
# ------------------------------
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🏠 House Price Prediction App")
st.write("Enter the details of the house to get an estimated price.")

# ------------------------------stream
# Input fields for features
# (⚡ Replace with the same features you used in training)
# ------------------------------
area = st.number_input("Area (sq ft)", min_value=500, max_value=10000, step=50)
bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
stories = st.number_input("Number of Stories", min_value=1, max_value=4, step=1)
parking = st.number_input("Number of Parking spaces", min_value=0, max_value=5, step=1)

mainroad = st.selectbox("Near Main Road?", ["Yes", "No"])
guestroom = st.selectbox("Has Guestroom?", ["Yes", "No"])
basement = st.selectbox("Has Basement?", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot Water Heating?", ["Yes", "No"])
airconditioning = st.selectbox("Air Conditioning?", ["Yes", "No"])
prefarea = st.selectbox("Preferred Area?", ["Yes", "No"])

# ------------------------------
# Convert inputs to a dataframe
# ------------------------------
input_data = pd.DataFrame({
    "area": [area],
    "bedrooms": [bedrooms],
    "bathrooms": [bathrooms],
    "stories": [stories],
    "parking": [parking],
    "mainroad": [1 if mainroad == "Yes" else 0],
    "guestroom": [1 if guestroom == "Yes" else 0],
    "basement": [1 if basement == "Yes" else 0],
    "hotwaterheating": [1 if hotwaterheating == "Yes" else 0],
    "airconditioning": [1 if airconditioning == "Yes" else 0],
    "prefarea": [1 if prefarea == "Yes" else 0]
})

# ------------------------------
# Prediction
# ------------------------------
if st.button("Predict House Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"🏡 Estimated House Price: ₹ {prediction:,.2f}")


