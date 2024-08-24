# Import required libraries
from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Vision Bot Demo")

st.header("Gemini Application")

# Input field for the Google API Key
api_key = st.text_input("Enter Your Gemini API Key: ", type="password")

# Input prompt from the user
input_text = st.text_input("Input Prompt: ", key="input")

# File uploader to allow users to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Button to submit the request
submit = st.button("Tell me about the image")

# if the streamlit button is clicked, configure the API key and get the Gemini AI response
if submit and api_key and image is not None:
    os.environ["GOOGLE_API_KEY"] = api_key
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    response = get_gemini_response(input_text, image)
    st.subheader("The Response is:")
    st.write(response)

# Function to load Gemini AI model and get the reponse
def get_gemini_response(input_text, image)
    model = genai.GenerativeModel("gemini_pro_vision")
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text
