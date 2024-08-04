import streamlit as st

st.set_page_config(layout= "wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("IMAGES/photo.png")

with col2:
    st.title("Akash Kumar")
    content = """
    I am a Data professional """
    st.info(content)