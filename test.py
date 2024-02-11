import streamlit as st
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
import numpy as np
import cv2


def main():
    st.title("GURU PRASAATH OCR")
    st.header("Choose an image")
    uploaded_file = st.file_uploader("Upload Your Image",type=["jpg","png"])
    img = np.array(Image.open(uploaded_file))
    st.image(img)
    st.write("Hi")
    text = pytesseract.image_to_string(img)
    st.write("Processing")
    print(text)
    st.write(text)

        
       





if __name__ == "__main__":
    main()
