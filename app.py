import streamlit as st


#code---

st.set_page_config(page_title="Vadarly",page_icon=":part_alternation_mark:",layout="wide")

#image---
image_path= https://th.bing.com/th/id/OIP._dP2SPVcLwJ-r_uKSsbpkwHaEK?rs=1&pid=ImgDetMain
st.image(image_path,use_column_width=True)

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



