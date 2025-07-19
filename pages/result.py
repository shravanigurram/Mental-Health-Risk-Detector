# pages/result.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Prediction Result", layout="centered")

st.title("📊 Your Mental Health Risk Result")

# Check if prediction exists
if "prediction" not in st.session_state or "probability" not in st.session_state:
    st.warning("⚠️ Please complete the form first!")
    st.page_link("pages/app.py", label="⬅️ Go to Form")
    st.stop()

prediction = st.session_state.prediction
probability = st.session_state.probability

if prediction == 1:
    st.error(f"⚠️ **High risk** of mental health issues.\n\n🧠 Confidence: `{probability:.2f}`")
    st.markdown("#### 🛡️ Recommended Actions:")
    st.markdown("- 💬 Speak with a licensed therapist or counselor.")
    st.markdown("- 🧘‍♀️ Consider mindfulness or wellness programs.")
    st.markdown("- 🏥 [Find Mental Health Professionals](https://www.findahelpline.com)")
    st.markdown("- 📱 [Download Mindfulness Apps](https://www.headspace.com)")

    st.markdown("#### 📈 Risk Confidence Visual")
    fig, ax = plt.subplots()
    ax.bar(['Low Risk', 'High Risk'], [1 - probability, probability], color=['green', 'red'])
    ax.set_ylabel('Confidence')
    st.pyplot(fig)

else:
    st.success(f"✅ **Low risk**. Great job!\n\n🧠 Confidence: `{probability:.2f}`")
    st.markdown("Keep taking care of your mental health! 💚")

    st.markdown("#### 📈 Confidence Chart")
    fig, ax = plt.subplots()
    ax.bar(['Low Risk', 'High Risk'], [probability, 1 - probability], color=['green', 'gray'])
    ax.set_ylabel('Confidence')
    st.pyplot(fig)

# Feedback option
feedback = st.radio("🔄 Was this prediction accurate for you?", ["Yes", "No"])
if feedback == "No":
    df = pd.DataFrame([st.session_state.user_input])
    df["model_prediction"] = prediction
    df["user_feedback"] = "Wrong"
    df.to_csv("wrong_predictions_log.csv", mode='a', index=False)
    st.warning("📩 Thanks! Your feedback has been recorded 🙏")

st.page_link("pages/app.py", label="🔁 Restart & Try Again", icon="🏠")


