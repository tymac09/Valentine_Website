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
st.markdown('<h1 class="big-heading">Saigon Memories 🌆</h1>', unsafe_allow_html=True)

# Function to resize images to a fixed size
def resize_image(image, target_size=(800, 600)):  
    return image.resize(target_size, Image.ANTIALIAS)

# Load Top Image (Using GitHub Raw URL)
top_image_url = "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_heading.jpeg"

try:
    response = requests.get(top_image_url)
    top_image = Image.open(BytesIO(response.content))
    top_image = resize_image(top_image)  # Resize before displaying
    st.image(top_image, use_container_width=True)
except Exception as e:
    st.write("⚠️ Top image not found or failed to load.")

# List of Image URLs (Stored in GitHub)
image_urls = [
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_1.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_2.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_3.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_4.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_5.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_6.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_7.JPG",
    "https://raw.githubusercontent.com/tymac09/Valentine_Website/main/pictures/saigon_8.JPG"
]

# Messages for each image
messages = [
    "I love you so much my baby. I know we are not together for Valentine but I want you to know we will be together soon.",
    "So here’s a trip down memory lane.",
    "Our time together in the city was amazing and lovely.",
    "In the city that never sleeps, my love for you will never stop."
]

# Use 3 columns (Left Image, Message, Right Image)
for i in range(4):  # 4 rows, 2 images per row (left & right)
    col1, col2, col3 = st.columns([1, 1, 1])  # Three equal columns

    with col1:  # Left Column
        try:
            response = requests.get(image_urls[i])
            image = Image.open(BytesIO(response.content))
            image = resize_image(image)  # Resize before displaying
            st.image(image, use_container_width=True)
        except Exception as e:
            st.write("⚠️ Image not found.")

    with col2:  # Middle Column (Text Box)
        st.markdown(f'<div class="message-box">{messages[i]}</div>', unsafe_allow_html=True)

    with col3:  # Right Column
        try:
            response = requests.get(image_urls[i + 4])  # Ensuring correct indexing for right images
            image = Image.open(BytesIO(response.content))
            image = resize_image(image)  # Resize before displaying
            st.image(image, use_container_width=True)
        except Exception as e:
            st.write("⚠️ Image not found.")
