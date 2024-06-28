import streamlit as st

st.set_page_config(page_title="AI Project",page_icon=":joy:",layout="wide")

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
        -This is our project
        -line1
        -line2
        -line3""")
        st.write("other things...")
