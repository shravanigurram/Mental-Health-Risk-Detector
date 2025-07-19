
# app.py
import streamlit as st
from utils import preprocess_input, predict_risk

st.set_page_config(page_title="Mental Health Prediction", layout="centered")
st.title("📝 Mental Health Risk Assessment")

st.subheader("Quick Survey About Your Workplace Experience")

st.markdown("""
- Answer a few quick questions.
- Get a personalized mental health risk report.
- Takes less than 2 minutes.
- Your data stays private.
- Powered by AI for smarter insights.
""")


# Initialize session state
for key in ['personal_done', 'work_done', 'attitude_done', 'user_input']:
    if key not in st.session_state:
        st.session_state[key] = False if key != 'user_input' else {}

# ------------------- SECTION 1 -------------------
with st.expander("👤 Personal Details", expanded=not st.session_state.personal_done):
    with st.form("personal_form"):
        st.session_state.user_input['Age'] = st.number_input("How old are you?", min_value=12, max_value=100, value=25)
        st.session_state.user_input['Gender'] = st.selectbox("What is your gender?", ['Male', 'Female', 'Other'])
        st.session_state.user_input['self_employed'] = st.selectbox("Are you currently self-employed?", ['Yes', 'No'])
        st.session_state.user_input['family_history'] = st.selectbox("Do you have a family history of mental health issues?", ['Yes', 'No'])
        personal_submit = st.form_submit_button("✅ Save Personal Details")

    if personal_submit:
        st.success("✅ Personal details saved!")
        st.session_state.personal_done = True


# ------------------- SECTION 2 -------------------
if st.session_state.personal_done:
    with st.expander("🏢 Work Environment", expanded=not st.session_state.work_done):
        with st.form("work_form"):
            st.session_state.user_input['work_interfere'] = st.selectbox("How often does your work affect your mental health?", ['Never', 'Rarely', 'Sometimes', 'Often'])
            st.session_state.user_input['no_employees'] = st.selectbox("How big is your company?", ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000'])
            st.session_state.user_input['remote_work'] = st.selectbox("Do you work remotely (from home)?", ['Yes', 'No'])
            st.session_state.user_input['tech_company'] = st.selectbox("Is your company in the tech industry?", ['Yes', 'No'])
            st.session_state.user_input['benefits'] = st.selectbox("Does your employer offer mental health benefits?", ['Yes', 'No', "I don't know"])
            st.session_state.user_input['care_options'] = st.selectbox("Are you aware of available mental health care options?", ['Yes', 'No', "Not sure"])
            st.session_state.user_input['wellness_program'] = st.selectbox("Is there any wellness or mental health program at your company?", ['Yes', 'No', "I don't know"])
            st.session_state.user_input['seek_help'] = st.selectbox("Do you know how to seek help for mental health at work?", ['Yes', 'No', "I don't know"])
            st.session_state.user_input['anonymity'] = st.selectbox("Is it possible to get help anonymously at your workplace?", ['Yes', 'No', "I don't know"])
            st.session_state.user_input['leave'] = st.selectbox("How easy is it to take mental health-related leave?", ['Very easy', 'Somewhat easy', 'Somewhat difficult', 'Very difficult', "I don't know"])
            work_submit = st.form_submit_button("✅ Save Work Details")

        if work_submit:
            st.success("✅ Work environment details saved!")
            st.session_state.work_done = True

# ------------------- SECTION 3 -------------------
if st.session_state.work_done:
    with st.expander("🧣 Attitudes and Perception", expanded=not st.session_state.attitude_done):
        with st.form("attitude_form"):
            st.session_state.user_input['mental_health_consequence'] = st.selectbox("Could talking about mental health affect your job?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['phys_health_consequence'] = st.selectbox("Could talking about physical health affect your job?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['coworkers'] = st.selectbox("Are you comfortable talking about mental health with coworkers?", ['Yes', 'No', "Only some of them"])
            st.session_state.user_input['supervisor'] = st.selectbox("Are you comfortable discussing mental health with your manager/supervisor?", ['Yes', 'No', "Only some of them"])
            st.session_state.user_input['mental_health_interview'] = st.selectbox("Would you feel okay discussing mental health during a job interview?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['phys_health_interview'] = st.selectbox("Would you feel okay discussing physical health during a job interview?", ['Yes', 'No', "Maybe"])
            st.session_state.user_input['mental_vs_physical'] = st.selectbox("In your opinion, which is taken more seriously at work?", ['Mental Health', 'Physical Health', "I don't know"])
            st.session_state.user_input['obs_consequence'] = st.selectbox("Have you seen anyone face problems for discussing mental health at work?", ['Yes', 'No'])
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


