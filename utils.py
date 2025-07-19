'''import joblib
import numpy as np
import pandas as pd

# Load models and encoders
xgb_model = joblib.load('models/xgboost_model.pkl')
rf_model = joblib.load('models/random_forest_model.pkl')
label_encoders = joblib.load('models/label_encoders.pkl')

# Define expected columns (must match training)
expected_columns = [
    'Age', 'Gender', 'self_employed', 'family_history', 'work_interfere',
    'no_employees', 'remote_work', 'tech_company', 'benefits',
    'care_options', 'wellness_program', 'seek_help', 'anonymity',
    'leave', 'mental_health_consequence', 'phys_health_consequence',
    'coworkers', 'supervisor', 'mental_health_interview',
    'phys_health_interview', 'mental_vs_physical', 'obs_consequence'
]

# Preprocessing function
def preprocess_input(user_input_dict):
    input_df = pd.DataFrame([user_input_dict])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = np.nan

    # Ensure numeric age
    input_df['Age'] = pd.to_numeric(input_df['Age'], errors='coerce')
    input_df['Age'].fillna(30, inplace=True)

    # Encode categorical columns
    for col in expected_columns:
        if col in label_encoders:
            le = label_encoders[col]
            try:
                input_df[col] = le.transform(input_df[col])
            except:
                input_df[col] = le.transform([le.classes_[0]])[0]

    return input_df[expected_columns]

# Prediction function (ensemble of XGB + RF)
def predict_risk(preprocessed_input):
    pred_xgb = xgb_model.predict_proba(preprocessed_input)[:, 1]
    pred_rf = rf_model.predict_proba(preprocessed_input)[:, 1]

    avg_proba = (pred_xgb + pred_rf) / 2
    label = (avg_proba >= 0.5).astype(int)

    return label[0], avg_proba[0]
'''


import joblib
import numpy as np
import pandas as pd
import os

# Path fix
model_path = 'models'
xgb_model = joblib.load(os.path.join(model_path, 'xgboost_model.pkl'))
rf_model = joblib.load(os.path.join(model_path, 'random_forest_model.pkl'))
label_encoders = joblib.load(os.path.join(model_path, 'label_encoders.pkl'))

# Expected input features
expected_columns = [
    'Age', 'Gender', 'self_employed', 'family_history', 'work_interfere',
    'no_employees', 'remote_work', 'tech_company', 'benefits',
    'care_options', 'wellness_program', 'seek_help', 'anonymity',
    'leave', 'mental_health_consequence', 'phys_health_consequence',
    'coworkers', 'supervisor', 'mental_health_interview',
    'phys_health_interview', 'mental_vs_physical', 'obs_consequence'
]

def preprocess_input(user_input_dict):
    input_df = pd.DataFrame([user_input_dict])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = np.nan

    # Handle numeric
    input_df['Age'] = pd.to_numeric(input_df['Age'], errors='coerce')
    input_df['Age'].fillna(30, inplace=True)

    # Encode categorical values
    for col in expected_columns:
        if col in label_encoders:
            le = label_encoders[col]
            try:
                input_df[col] = le.transform(input_df[col])
            except:
                input_df[col] = le.transform([le.classes_[0]])[0]

    return input_df[expected_columns]

def predict_risk(preprocessed_input):
    pred_xgb = xgb_model.predict_proba(preprocessed_input)[:, 1]
    pred_rf = rf_model.predict_proba(preprocessed_input)[:, 1]

    avg_proba = (pred_xgb + pred_rf) / 2
    label = (avg_proba >= 0.5).astype(int)

    return label[0], avg_proba[0]
