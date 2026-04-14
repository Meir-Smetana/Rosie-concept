import streamlit as st
import streamlit.components.v1 as components

# This makes the app fill the whole screen
st.set_page_config(
    page_title="DesignFlow Concept",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# This CSS hides the "Streamlit" bars so it looks like a professional app
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {margin: 0; padding: 0;}
    iframe {border-radius: 0px;}
    </style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# This part opens your index.html and displays it
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # We set the height to 1000 so she can scroll through her projects
    components.html(html_content, height=1000, scrolling=True)
except FileNotFoundError:
    st.error("Wait! You forgot to upload the index.html file to GitHub.")
