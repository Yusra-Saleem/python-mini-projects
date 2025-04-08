import streamlit as st
import qrcode
from PIL import Image
import cv2
import numpy as np
import io
import json
from streamlit_lottie import st_lottie
import tempfile

# Load animation function
def load_lottie(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Generate QR Code (Black and White)
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,  # Set QR Code version (higher version = larger code)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Use higher error correction for better recovery
        box_size=20,  # Increase box size for better readability
        border=6,  # Keep border size consistent
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')  # Black and white colors
    return img

# Decode QR Code
def decode_qr(uploaded_file):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    
    # Convert image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply binary thresholding to improve contrast for detection
    _, thresh_img = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
    
    # Resize the image for better detection (double the size)
    resized_img = cv2.resize(thresh_img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
    
    # Detect and decode the QR code
    detector = cv2.QRCodeDetector()
    data, vertices, _ = detector.detectAndDecode(resized_img)
    
    return data, img

# Page config
st.set_page_config(page_title="QR Code Web App", layout="centered")

# Custom CSS for better UI and light animation background
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f0c29, #302b63, #24243e);
    color: white;
}
h1 {
    color: #00ffff;
    text-align: center;
}
.stButton > button {
    background-color: #00ffcc;
    color: black;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    width: 100%;
}
.stFileUploader {
    background-color: #00ffcc;
    color: black;
    border-radius: 10px;
    padding: 10px 20px;
}
.stFileUploader > div > div {
    background-color: #00ffcc;
}
.stTextInput input {
    background-color: #222;
    color: white;
    border: 1px solid #00ffcc;
}
.stTextInput label {
    color: #00ffcc;
}
.stDownloadButton > button {
    background-color: #00ffcc;
    color: black;
    border-radius: 10px;
    padding: 10px 20px;
}
.stLottie {
    background-color: #ffffff;  /* Explicitly set white background for the animation */
    padding: 10px;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);  /* Optional: add a subtle shadow to the animation container */
}
/* Force tab styling overrides */
div[role="tablist"] > div[role="tab"] {
    color: #00ffcc !important;  /* Ensure text color is bright enough */
    font-weight: bold !important;
    font-size: 18px !important;
    background-color: transparent !important;
    padding: 12px 24px !important;
    border-radius: 8px !important;
    border: 1px solid #00ffcc !important;  /* Add border for better visibility */
}

div[role="tablist"] > div[role="tab"]:hover {
    background-color: #302b63 !important;  /* Ensure hover background color provides contrast */
}

div[role="tablist"] > div[role="tab"][aria-selected="true"] {
    color: #ffffff !important;  /* Ensure active tab text color is visible */
    background-color: #00cc99 !important;  /* Ensure active tab background color provides contrast */
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# Load animation
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st_lottie(load_lottie("qr_anim.json"), height=200)

# Title
st.markdown("## 🌀 QR Code Generator & Decoder")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["✨ Generate QR", "🔍 Decode QR"])

# Tab 1 - Generate QR
with tab1:
    st.markdown("### Generate QR Code")
    user_input = st.text_input("Enter Text or URL to generate QR")
    if st.button("Generate QR Code"):
        if user_input:
            img = generate_qr(user_input)
            
            # Save image to a temporary buffer
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)  # Go to the start of the buffer
            
            # Display the image from the byte buffer
            st.image(buf, caption="Generated QR Code", use_container_width=True)
            
            # Use a temporary file to allow re-uploading it for decoding
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_file.write(buf.getvalue())
                temp_file_path = temp_file.name
            
            # Provide a download link
            st.download_button("Download QR", buf, file_name="qr_code.png", mime="image/png")

# Tab 2 - Decode QR
with tab2:
    st.markdown("### Upload QR Code to Decode")
    uploaded = st.file_uploader("Upload QR Code Image", type=["png", "jpg", "jpeg"])
    
    if uploaded:
        result, image = decode_qr(uploaded)
        
        # Convert the image from BGR to RGB (OpenCV uses BGR by default)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Display the image
        st.image(image_rgb, caption="Uploaded QR Code", use_container_width=True)
        
        if result:
            st.success("Decoded Data:")
            st.code(result)
        else:
            st.error("No QR Code Detected. Please check if the image contains a valid QR code.")
