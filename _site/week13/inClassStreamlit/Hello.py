import streamlit as st

st.set_page_config(
    page_title="Hello", 
    page_icon=":grinning:"
)
st.sidebar.success("Select a Page")

st.header('Multi-page App')

st.markdown(""" Reorg of our App to multiple pages.""")