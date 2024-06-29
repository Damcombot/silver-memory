import streamlit as st
import requests
from PIL import Image

#code---

st.set_page_config(page_title="Vadarly",page_icon=":part_alternation_mark:",layout="wide")
img_contact= Image.open("C:\Users\Jmbli\OneDrive\Documents\GitHub\silver-memory\Images\hellopic.jpeg")

#hidder--
hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#hidder2--
hide_github_icon = """
<style>
    #GithubIcon {
        visibility: hidden;
    }
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


#Header---
with st.container():
            st.title(""" Welcome to _:blue[Vadarly]_ """)
            st.header("Vadarly is a ***voice assistant*** ")
            st.divider()
with st.container():
            left_column,right_column = st.columns(2)
            with left_column:
                        st.write("It uses :blue-background[NLP] and :red-background[CV] ")
                        st.write("It can predict the ***presence*** of user ")
            image_column,text_column = st.columns((1,2))
            with image_column:
                        st.image(img_contact)
with st.echo():
            def example():
              return "This works!!"
            st.write(example())
            
