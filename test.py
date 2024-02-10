import streamlit as st
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
import numpy as np
import cv2


def main():
    st.title("GURU PRASAATH OCR")
    # st.markdown("*Streamlit* is **really** ***cool***.")
    st.header("Choose an image")
    uploaded_file = st.file_uploader("Upload an image file",type=["jpg","png"])
    if uploaded_file is not None:
        try:
            img = np.array(Image.open(uploaded_file))
            st.image(img)
            st.write("Processing..")
            text = pytesseract.image_to_string(img)
            print(text)
            st.write(text)
            # Load the input image

# Check if the image is loaded successfully
            # if img is None:
                # print("Error: Could not load the image.")
    # Add appropriate error handling or exit the program if necessary

# Assuming 'img' is your input image

            # cv2norm_img = np.zeros((img.shape[0], img.shape[1]))

# Correct the variable name to cv2norm_img in the following line
            # img = cv2.normalize(img, cv2norm_img, 0, 255, cv2.NORM_MINMAX)

# Convert the image to uint8 before using cv2.threshold
            # img = img.astype(np.uint8)

# Correct the thresholding line
    # _, img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

# Correct GaussianBlur parameters
            # img = cv2.GaussianBlur(img, (5, 5), 0)
            
            # text = pytesseract.image_to_string(img)
            # print(text)
            
            # st.write(text)
            
            
            # if st.button("Stream data"):
            #     st.write(stream_data(text))

# This one is for normal image
            # filename = 'D:/OCR/test4.png'


# Output Line





        except Exception as e:
            print(e)

# def stream_data(guru):
#     for word in guru.split():
#         yield word + ","
#         time.sleep(1)






if __name__ == "__main__":
    main()
