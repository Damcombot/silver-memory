import streamlit as st


#code---

st.set_page_config(page_title="Vadarly",page_icon=":part_alternation_mark:",layout="wide")

#images store---
image_path= "https://th.bing.com/th/id/OIP._dP2SPVcLwJ-r_uKSsbpkwHaEK?rs=1&pid=ImgDetMain"


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
#camera-roll-test-- 

#picture = st.camera_input("Take a picture")

#if picture:
    #st.image(picture)

#code-box--
st.code("""def fun():
         print(5+6)""")

#image1---
col1 , col2 = st.columns([2, 1])
with col2:
            st.image(image_path,caption="Just a normal image")
with col1:
            st.write("Random Text")



