import streamlit as st
import google.generativeai as genai

# Setup the AI
st.set_page_config(page_title="Creator Magic", page_icon="🚀")
st.title("🚀 Creator Caption Magic")

# Sidebar for the API Key
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # The Input Box
    user_input = st.text_area("What is your post or video about?", placeholder="e.g. My new coffee recipe")

    # The Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("IG Caption"):
            response = model.generate_content(f"Write a viral Instagram caption for: {user_input}")
            st.info(response.text)
    with col2:
        if st.button("YT Description"):
            response = model.generate_content(f"Write a YouTube description for: {user_input}")
            st.info(response.text)
    with col3:
        if st.button("Bio Idea"):
            response = model.generate_content(f"Write a cool bio for a creator who does: {user_input}")
            st.info(response.text)
else:
    st.warning("Please paste your API Key in the sidebar to begin!")
