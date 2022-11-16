from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Žaneta Tarabová - Vizáž a kozmetické služby",
                   page_icon=":sunny:", layout="wide")

# st.title("Domů")
# st.sidebar.success("Select Page Above.")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---------- USE LOCAL CSS ----------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ------- LOTTIE VARIABLE ----
lottie_coding = load_lottieurl(
    "https://assets3.lottiefiles.com/packages/lf20_IcG65O.json")
img_contact_form = Image.open("obrazky/obr1.png")
img_lottie_animation = Image.open("obrazky/obr2.png")


with st.container():
    st.subheader("Vítejte na mé stránce, jmenuji se Žaneta :wave:")
    st.title("Vizážistka a kozmetička")
    st.write("Poskytujem kozmetické služby so zameraním na vizáž a poradenstvo, pracujem s čisto prírodou kozmetikou, neagresívnou a netestovanou na zvieratách")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Moje služby")
        st.write('##')
        st.write(
            """
            Text:
            - .........
            - .............
            - .................
            - .....................
            - ..........................

            """
        )

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")


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


# ---------- CONTACT FORM ----------
with st.container():

    # ----- ROZDELOVAC ------
    st.write("---")
    st.header("V prípade záujmu mi napíšte správu")

# ----- MEDZERA -----
    st.write("##")

# ---------- DOCUMENTATION https://https://formsubmit.co/ ----------
contact_form = """
<form action="https://formsubmit.co/zaneta.tarabova@gmail.com" method="POST">
<!--
     <input type="text" name="name" placeholder="Zadajte meno" required>
     <input type="email" name="email" placeholder="Zadajte email" required>
    -->     
     <textarea name="Správa" placeholder="Napíšte správu" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()

