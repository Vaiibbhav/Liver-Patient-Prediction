import streamlit as st
import pandas as pd
import joblib

# Load trained model (correct file name)
model = joblib.load("liver_best_model.joblib")

# Ensure we use the same feature names as training
expected_features = model.feature_names_in_

st.set_page_config(page_title="Liver Disease Prediction", page_icon="🩺", layout="centered")

st.title("🩺 Liver Disease Prediction App")
st.write("This app predicts whether a person is likely to have **Liver Disease** based on medical parameters.")

st.sidebar.header("Patient Input Features")

def user_input_features():
    age = st.sidebar.number_input("Age", 1, 100, 45)
    gender = st.sidebar.selectbox("Gender", ("Male", "Female"))
    tb = st.sidebar.number_input("Total Bilirubin", 0.0, 50.0, 1.0)
    db = st.sidebar.number_input("Direct Bilirubin", 0.0, 20.0, 0.3)
    alkphos = st.sidebar.number_input("Alkaline Phosphotase", 0, 2000, 200)
    sgpt = st.sidebar.number_input("Alamine Aminotransferase (SGPT)", 0, 2000, 30)
    sgot = st.sidebar.number_input("Aspartate Aminotransferase (SGOT)", 0, 2000, 40)
    tp = st.sidebar.number_input("Total Proteins", 0.0, 10.0, 6.5)
    alb = st.sidebar.number_input("Albumin", 0.0, 6.0, 3.5)
    ag_ratio = st.sidebar.number_input("Albumin and Globulin Ratio", 0.0, 3.0, 1.0)

    data = {
        "Age": age,
        "Gender": gender,
        "Total_Bilirubin": tb,
        "Direct_Bilirubin": db,
        "Alkaline_Phosphotase": alkphos,
        "Alamine_Aminotransferase": sgpt,
        "Aspartate_Aminotransferase": sgot,
        "Total_Proteins": tp,
        "Albumin": alb,
        "Albumin_and_Globulin_Ratio": ag_ratio,
    }
    df = pd.DataFrame(data, index=[0])

    # Align with expected features
    df = df.reindex(columns=expected_features, fill_value=0)

    return df

input_df = user_input_features()

st.subheader("Patient Data")
st.write(input_df)

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ The model predicts **Liver Disease**")
    else:
        st.success("✅ The model predicts **No Liver Disease**")
