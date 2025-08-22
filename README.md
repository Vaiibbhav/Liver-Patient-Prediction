# 🩺 Liver Patient Prediction (PRCP-1007)

## 📌 Project Overview
This project aims to predict whether a patient has liver disease based on demographic and biochemical test data using Machine Learning.  
The model was trained on the **Indian Liver Patient Dataset (ILPD)** and deployed with **Streamlit** for interactive predictions.  

---

## 📂 Dataset
- **Source:** Indian Liver Patient Dataset (UCI Repository)  
- **Records:** 583  
- **Features:**
  - Age, Gender
  - Total Bilirubin, Direct Bilirubin
  - Alkaline Phosphotase, SGPT, SGOT
  - Total Proteins, Albumin, A/G Ratio  
- **Target Variable:**  
  - `1` → Liver Disease  
  - `2` → No Liver Disease  

---

## ⚙️ Project Workflow
1. **Data Preprocessing**
   - Handle missing values
   - Encode categorical features
   - Scale numerical features
   - Apply SMOTE for class imbalance
2. **Exploratory Data Analysis (EDA)**
   - Distribution plots
   - Boxplots for feature vs target
   - Correlation analysis
3. **Modeling**
   - Compared Logistic Regression, Random Forest, XGBoost
   - Hyperparameter tuning with GridSearchCV
   - Final Model: **Random Forest Classifier**
4. **Evaluation**
   - Accuracy, Precision, Recall, F1-score
   - SHAP for feature importance
5. **Deployment**
   - Built a Streamlit app (`app.py`) for local prediction

---

## 📊 Results & Insights
- Dataset is imbalanced (~71% patients with liver disease).
- Random Forest with SMOTE gave the best balance between precision and recall.
- Important predictors: **Bilirubin levels, SGOT/SGPT enzymes, Age**.
- The model is capable of early detection and can assist in preventive healthcare.

---
