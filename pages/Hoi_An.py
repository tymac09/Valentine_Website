import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Custom CSS for styling
st.markdown( 
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');
        .stApp { background-color: #FFD1DC; }
        .big-heading {
            font-size: 75px !important;
            font-weight: bold !important;
            text-align: center;
            color: #000000 !important;
            margin-bottom: 30px;
            font-family: 'Great Vibes', cursive !important;
        }
        .message-box {
            background-color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #8B0000;
            width: 100%;
            margin-top: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown('<h1 class="big-heading">Hoi An Memories 🌊</h1>', unsafe_allow_html=True)

# Function to resize images to a fixed size
def resize_image(image, target_size=(800, 600)):  
    return image.resize(target_size, Image.ANTIALIAS)

# Top Image
top_image_url = "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_top.JPG"

try:
    response = requests.get(top_image_url)
    top_image = Image.open(BytesIO(response.content))
    top_image = resize_image(top_image)  # Resize before displaying
    st.image(top_image, use_container_width=True)
except Exception as e:
    st.write("⚠️ Top image not found or failed to load.")

# List of Image URLs
image_urls = [
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_1.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_2.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_3.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_4.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_5.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_6.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_7.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_8.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_9.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine-Web/main/pictures/hoian_10.JPG"
]

# Messages for each image
messages = [
    "I love you so much more baby.",
    "Our trip to Hoi An was amazing and I loved every second and every day being with you.",
    "I remember our walked on the beach and feeling the nice breeze and holding your hands.",
    "Going into the beach and holding you in my arm is a memory I will never forget.",
    "Thank you for being my amazing love, my beautiful girlfriend, and my perfect wife. You are the love of my life."
]

# Display images with resizing
for i in range(5):  
    col1, col2, col3 = st.columns([1, 1, 1]) 

    with col1:  
        try:
            response = requests.get(image_urls[i])
            image = Image.open(BytesIO(response.content))
            image = resize_image(image)  # Resize before displaying
            st.image(image, use_container_width=True)
        except Exception as e:
            st.write("⚠️ Image not found.")

    with col2:  
        st.markdown(f'<div class="message-box">{messages[i]}</div>', unsafe_allow_html=True)

    with col3:  
        try:
            response = requests.get(image_urls[i + 5])
            image = Image.open(BytesIO(response.content))
            image = resize_image(image)  # Resize before displaying
            st.image(image, use_container_width=True)
        except Exception as e:
            st.write("⚠️ Image not found.")
