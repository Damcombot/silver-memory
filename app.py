import streamlit as st


#code---

st.set_page_config(page_title="Vadarly",page_icon=":chart:",layout="wide")

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
    st.subheader("Hi!,Welcome to our AI project :wave:")
    st.title("""It uses open cv and NLP to provide output""")
    st.write("[Learn more >](https://blinderoggy.wixsite.com/vadarly)")

with st.container():
    st.write("---")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("This is a column;")
        st.write("something..")
        st.write("""HELLO ALL!!!
        \n-This is our project
        \n-line1
        \n-line2
        \n-line3""")
        st.write("other things...")
