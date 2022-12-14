from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.header("Moje projekty a ukázky práce")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ------- LOTTIE VARIABLE ----
lottie_coding = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_IcG65O.json")

# ---------- IMAGES ----------
img_contact_form = Image.open("obrazky/obr1.png")
img_lottie_animation = Image.open("obrazky/obr2.png")

# ---------- VIDEO ----------
video_file = open('video/video.mp4', 'rb')
video_bytes = video_file.read()


# ------ MOJE PROJEKTY A PRACA ------
with st.container():
    st.write("---")
    st.header("Moje Projekty a Práca")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)

with st.container():
    video_file, text_column = st.columns((1, 2))
    with video_file:
        st.video(video_bytes)
