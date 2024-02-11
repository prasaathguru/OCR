import streamlit as st
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
import numpy as np
import cv2


def main():
    st.title("GURU PRASAATH OCR")
    st.header("Choose an image")
    uploaded_file = st.file_uploader("",type=["jpg","png"])
    if uploaded_file is not None:
        try:
            img = np.array(Image.open(uploaded_file))
            st.image(img)
            text = pytesseract.image_to_string(img)
            print(text)
            st.write(text)

        
        except Exception as e:
            print(e)






if __name__ == "__main__":
    main()
