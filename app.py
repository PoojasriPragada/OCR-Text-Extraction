import streamlit as st
import pytesseract
from PIL import Image
import cv2
import tempfile
import pdf2image
import numpy as np  # <-- Add this import

st.set_page_config(page_title="OCR Extractor", layout="centered")
st.title("📄 OCR Text Extractor")
st.markdown("Upload an image or PDF or use your webcam to extract printed text.")

# Sidebar
st.sidebar.title("Upload Options")
upload_option = st.sidebar.radio("Select Input Source", ["Image Upload", "PDF Upload", "Webcam"])

text_output = ""

def extract_text_from_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

if upload_option == "Image Upload":
    uploaded_file = st.file_uploader("Upload an image (JPG, PNG)", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)
        text_output = extract_text_from_image(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))

elif upload_option == "PDF Upload":
    uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])
    if uploaded_pdf:
        with tempfile.TemporaryDirectory() as path:
            images = pdf2image.convert_from_bytes(uploaded_pdf.read(), dpi=200, output_folder=path)
            for i, img in enumerate(images):
                st.image(img, caption=f"Page {i+1}")
                text_output += pytesseract.image_to_string(img)

elif upload_option == "Webcam":
    picture = st.camera_input("Take a photo")
    if picture:
        image = Image.open(picture).convert("RGB")
        st.image(image, caption="Captured Image")
        text_output = extract_text_from_image(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR))

if text_output:
    st.text_area("Extracted Text", value=text_output, height=300)
    if st.download_button("Download as .txt", text_output, file_name="extracted_text.txt"):
        st.success("File ready for download!")