import gmaps
import requests
import streamlit as st
from PIL import Image
import folium


with st.container():

    st.header("Kontakt")
    st.write(
        """
            - Telefón: +421 123 456 
            - EMAIL: meno@gmail.com
            - SKYPE
            - .....................
            - ..........................




            """
    )

# ---------- MAPA ------------
m = folium.Map(location=[50.075539, 14.437800],
               zoom_start=20, width=500, height=500, position=str)
m

# ----- MEDZERA -----
st.write("##")

# ---------- FORMAT CONTACT FORMu ----------


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
# -----------------------------------------------------------------------


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

# ---------- UMIESTNENIE NA STRANKU ----------
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
