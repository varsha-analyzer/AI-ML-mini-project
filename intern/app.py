import streamlit as st
import pickle
st.write("Welcome")
model = pickle.load(open("heart_disease_model.pkl","rb"))
st.write("Model Loaded Successfully!")
st.title("Heart Disease Prediction")
model = pickle.load(open("heart_disease_model.pkl", "rb"))
st.success("Model Loaded Successfully!")
age = st.number_input("Age")
sex = st.number_input("Sex")
cp = st.number_input("Chest Pain Type")
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.number_input("Fasting Blood Sugar")
restecg = st.number_input("Resting ECG")
thalach = st.number_input("Maximum Heart Rate")
exang = st.number_input("Exercise Induced Angina")
oldpeak = st.number_input("Old Peak")
slope = st.number_input("Slope")
ca = st.number_input("CA")
thal = st.number_input("Thal")
with open("heart_disease_model.pkl", "rb") as file:
    rf = pickle.load(file)
a1 = st.number_input("Enter age")
a2 = st.number_input("Enter sex")
a3 = st.number_input("Enter cp")
a4 = st.number_input("Enter trestbps")
a5 = st.number_input("Enter chol")
a6 = st.number_input("Enter fbs")
a7 = st.number_input("Enter restecg")
a8 = st.number_input("Enter thalach")
a9 = st.number_input("Enter exang")
a10 = st.number_input("Enter oldpeak")
a11 = st.number_input("Enter slope")
a12 = st.number_input("Enter ca")
a13 = st.number_input("Enter thal")
if st.button("Predict"):

    final = [[a1, a2, a3, a4, a5, a6, a7,
              a8, a9, a10, a11, a12, a13]]

    result = rf.predict(final)

    st.write("Prediction:", result[0])

    if result[0] == 1:
        st.error("Heart Disease Detected")
    else:
        st.success("This person has no heart disease")
