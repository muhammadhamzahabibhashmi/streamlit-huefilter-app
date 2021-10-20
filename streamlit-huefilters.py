import streamlit as st
import cv2
import numpy as np

uploaded_file = st.file_uploader("Upload Image",type=['png','jpeg'])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    frame = opencv_image.copy()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l1 = st.sidebar.slider("Lower 1", min_value=0, max_value=255, step=1)
    h1 = st.sidebar.slider("Upper 1", min_value=0, max_value=255, step=1)
    l2 = st.sidebar.slider("Lower 2", min_value=0, max_value=255, step=1)
    h2 = st.sidebar.slider("Upper 2", min_value=0, max_value=255, step=1)
    l3 = st.sidebar.slider("Lower 3", min_value=0, max_value=255, step=1)
    h3 = st.sidebar.slider("Upper 3", min_value=0, max_value=255, step=1)
    erode1 = st.sidebar.slider("Erosion iteration", min_value=0, max_value=10, step=1)
    dilate1 = st.sidebar.slider("Dilation iteration", min_value=0, max_value=10, step=1)

    kernel = np.ones((5,5), np.uint8)
    lower_ = np.array([l1,l2,l3])
    upper_ = np.array([h1,h2,h3])

    mask = cv2.inRange(hsv, lower_, upper_)
    mask = cv2.erode(mask, kernel, iterations=erode1)
    mask = cv2.dilate(mask, kernel, iterations=dilate1)
    frame[mask == 255] = (255,255,255)
    st.image(mask, channels="Gray")
    st.image(frame, channels="BGR")
