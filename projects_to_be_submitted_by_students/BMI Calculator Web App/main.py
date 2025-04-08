import streamlit as st

# Set page title and layout
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .stApp {
        background-color: #F0F2F6;
    }
    .title {
        color: #4CAF50;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .info-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.1);
        text-align: center;
        font-size: 18px;
        color: #333;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
        width: 100%;
        border: none;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .motivation {
        text-align: center;
        font-size: 18px;
        color: #4CAF50;
        margin-top: 20px;
    }
    input[type="number"] {
        border: 2px solid #4CAF50 !important;
        border-radius: 5px !important;
        padding: 10px !important;
        font-size: 18px !important;
        box-sizing: border-box;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">💪 BMI Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="info-box">Easily calculate your <b>Body Mass Index (BMI)</b> and check your health category.</div>', unsafe_allow_html=True)

# Input fields
weight = st.number_input("🔹 Enter your weight (kg)", min_value=1.0, format="%.1f")
height = st.number_input("🔹 Enter your height (m)", min_value=0.5, format="%.2f")

# Calculate BMI button
if st.button("Calculate BMI", key="calculate", help="Click to calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.markdown(f'<div class="info-box">📝 Your BMI is: <b>{bmi:.2f}</b></div>', unsafe_allow_html=True)

        # Interpret the BMI category with colored messages
        if bmi < 18.5:
            st.warning("🔹 **Underweight** - You may need to gain weight for better health.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ **Normal Weight** - Great! You have a healthy weight.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ **Overweight** - Consider a healthier lifestyle.")
        else:
            st.error("🚨 **Obese** - You should consult a doctor or nutritionist.")
    else:
        st.error("❌ Please enter valid values for weight and height.")

# Extra motivation message
st.markdown('<div class="motivation">🏋️‍♂️ **Stay fit, eat healthy, and exercise regularly!**</div>', unsafe_allow_html=True)
