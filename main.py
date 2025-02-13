import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Custom CSS for styling
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

        /* Background color */
        .stApp {
            background-color: #FFD1DC;
        }

        /* Heading style */
        .big-heading {
            font-size: 75px !important;
            font-weight: bold !important;
            text-align: center;
            color: #000000 !important;
            margin-bottom: 50px;
            font-family: 'Great Vibes', cursive !important;
        }
        .lower-heading {
            font-size: 60px !important;
            font-weight: bold !important;
            text-align: center;
            color: #000000 !important;
            margin-bottom: 50px;
            font-family: 'Great Vibes', cursive !important; 
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<h1 class="big-heading">Happy Valentine</h1>', unsafe_allow_html=True)
st.markdown('<h1 class="lower-heading">My Love Nguyễn Hoàng Bảo Châu</h1>', unsafe_allow_html=True)

#  Load Home Page Image Using GitHub Raw URL
image_url = "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/home_page_pic.JPG"

try:
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    st.image(image,  use_container_width=True)  # Display image
except Exception as e:
    st.write("⚠️ Image not found. Please check the file path.")
