
# app.py
import streamlit as st
from utils import preprocess_input, predict_risk

st.set_page_config(page_title="Mental Health Prediction", layout="centered")
st.title("🧠 Mental Health Risk Predictor")

st.markdown("Welcome! This app predicts your mental health risk based on workplace conditions.")
st.markdown("👉 Please fill each section one by one. All sections must be completed before prediction.")

# Initialize session state
for key in ['personal_done', 'work_done', 'attitude_done', 'user_input']:
    if key not in st.session_state:
        st.session_state[key] = False if key != 'user_input' else {}

# ------------------- SECTION 1 -------------------
with st.expander("👤 Personal Details", expanded=not st.session_state.personal_done):
    with st.form("personal_form"):
        st.session_state.user_input['Age'] = st.number_input("Age", min_value=12, max_value=100, value=25)
        st.session_state.user_input['Gender'] = st.selectbox("Gender", ['Male', 'Female', 'Other'])
        st.session_state.user_input['self_employed'] = st.selectbox("Are you self-employed?", ['Yes', 'No'])
        st.session_state.user_input['family_history'] = st.selectbox("Family history of mental illness?", ['Yes', 'No'])
        personal_submit = st.form_submit_button("✅ Save Personal Details")

    if personal_submit:
        st.success("✅ Personal details saved!")
        st.session_state.personal_done = True

# ------------------- SECTION 2 -------------------
if st.session_state.personal_done:
    with st.expander("🏢 Work Environment", expanded=not st.session_state.work_done):
        with st.form("work_form"):
            st.session_state.user_input['work_interfere'] = st.selectbox("Does work interfere with mental health?", ['Never', 'Rarely', 'Sometimes', 'Often'])
            st.session_state.user_input['no_employees'] = st.selectbox("No. of employees in your company", ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'])
            st.session_state.user_input['remote_work'] = st.selectbox("Do you work remotely?", ['Yes', 'No'])
            st.session_state.user_input['tech_company'] = st.selectbox("Is it a tech company?", ['Yes', 'No'])
            st.session_state.user_input['benefits'] = st.selectbox("Mental health benefits?", ['Yes', 'No', "Don't know"])
            st.session_state.user_input['care_options'] = st.selectbox("Do you know care options?", ['Yes', 'No', "Not sure"])
            st.session_state.user_input['wellness_program'] = st.selectbox("Is there a wellness program?", ['Yes', 'No', "Don't know"])
            st.session_state.user_input['seek_help'] = st.selectbox("Do you know how to seek help?", ['Yes', 'No', "Don't know"])
            st.session_state.user_input['anonymity'] = st.selectbox("Is help anonymous?", ['Yes', 'No', "Don't know"])
            st.session_state.user_input['leave'] = st.selectbox("Ease of taking leave?", ['Very easy', 'Somewhat easy', 'Somewhat difficult', 'Very difficult', "Don't know"])
            work_submit = st.form_submit_button("✅ Save Work Details")

        if work_submit:
            st.success("✅ Work environment details saved!")
            st.session_state.work_done = True

# ------------------- SECTION 3 -------------------
if st.session_state.work_done:
    with st.expander("🧣 Attitudes and Perception", expanded=not st.session_state.attitude_done):
        with st.form("attitude_form"):
            st.session_state.user_input['mental_health_consequence'] = st.selectbox("Mental health consequences at work?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['phys_health_consequence'] = st.selectbox("Physical health consequences at work?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['coworkers'] = st.selectbox("Comfort discussing with coworkers?", ['Yes', 'No', "Some of them"])
            st.session_state.user_input['supervisor'] = st.selectbox("Comfort discussing with supervisor?", ['Yes', 'No', "Some of them"])
            st.session_state.user_input['mental_health_interview'] = st.selectbox("Would you discuss mental health in interview?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['phys_health_interview'] = st.selectbox("Would you discuss physical health in interview?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['mental_vs_physical'] = st.selectbox("Which is taken more seriously?", ['Yes', 'No', "Don't know"])
            st.session_state.user_input['obs_consequence'] = st.selectbox("Observed consequences of discussing mental health?", ['Yes', 'No'])
            attitude_submit = st.form_submit_button("✅ Save Attitude & Perception")

        if attitude_submit:
            st.success("✅ Attitudes and perception saved!")
            st.session_state.attitude_done = True


# ------------------- PREDICT & REDIRECT -------------------
if all([st.session_state.personal_done, st.session_state.work_done, st.session_state.attitude_done]):
    st.markdown("---")
    st.markdown("### 🎯 Ready to Predict Your Mental Health Risk")
    if st.button("🔍 Predict Mental Health Risk"):
        try:
            processed_input = preprocess_input(st.session_state.user_input)
            prediction, probability = predict_risk(processed_input)

            st.session_state.prediction = prediction
            st.session_state.probability = probability

            st.switch_page("pages/result.py")

        except Exception as e:
            st.error(f"🚨 Something went wrong: {e}")


