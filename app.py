import streamlit as st
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


#code---

st.set_page_config(page_title="AI Project",page_icon=":open_book:",layout="wide")

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
