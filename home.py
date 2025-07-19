import streamlit as st

st.set_page_config(page_title="Welcome", layout="wide")

# ---- Page Layout ----
st.markdown("<style>body { background-color: #f5f7fa; }</style>", unsafe_allow_html=True)

# Title and logo in 2 columns
left, right = st.columns([2, 1], gap="large")

with left:
    st.markdown("<center><h1 style='font-size: 40px;'>🧠 Mental Health Risk Predictor</h1></center>", unsafe_allow_html=True)
    st.markdown("""
                <br>
                <br>
        <center><p style='font-size:18px; line-height:1.6;'>
        Welcome to our <b>AI-powered</b> mental health risk prediction tool.<br><br>
        This app helps assess workplace mental health risks based on your responses.<br><br>
        It’s completely confidential, easy to use, and backed by research.
        </p></center>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Get Started", use_container_width=True):
        st.switch_page("pages/app.py")

with right:
    st.image("app_logo.png", width=300, caption="Mental Health Matters")

# ---- Stylish Footer ----



st.markdown("""
    
            
            <br>
            <br>
            <br>
    <hr style="border: none; height: 1px; background-color: #ddd; margin-top: 40px;">

    <div style='text-align: center; font-size: 14px; color: #555;'>
        Empowering Minds, One Prediction at a Time
        <br>
        Made with ❤️ by Shravani Gurram
        
    </div>
""", unsafe_allow_html=True)
