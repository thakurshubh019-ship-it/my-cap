import streamlit as st
import google.generativeai as genai

# Setup the AI
st.set_page_config(page_title="Creator Magic", page_icon="🚀")
st.title("🚀 Creator Caption Magic")

# Sidebar for the API Key
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # The Input Box
        user_input = st.text_area("What is your post or video about?", placeholder="e.g. My new coffee recipe")
        
        # The Buttons
        col1, col2, col3 = st.columns(3)
        
        # Function to generate content safely
        def generate_caption(prompt_text, instruction):
            if not prompt_text.strip():
                st.error("⚠️ Please enter content first!")
                return
            
            try:
                with st.spinner("✨ Creating your caption..."):
                    response = model.generate_content(f"{instruction} {prompt_text}")
                    if response and response.text:
                        st.success("✅ Caption generated successfully!")
                        st.info(response.text)
                    else:
                        st.error("❌ No response generated. Please try again.")
            except Exception as e:
                st.error(f"❌ Error generating caption: {str(e)}")
        
        with col1:
            if st.button("IG Caption"):
                generate_caption(user_input, "Write a viral Instagram caption for:")
        
        with col2:
            if st.button("YT Description"):
                generate_caption(user_input, "Write a YouTube description for:")
        
        with col3:
            if st.button("Bio Idea"):
                generate_caption(user_input, "Write a cool bio for a creator who does:")
    
    except Exception as e:
        st.error(f"❌ Configuration Error: Failed to initialize AI model. Please check your API key.")
        st.error(f"Details: {str(e)}")
else:
    st.warning("Please paste your API Key in the sidebar to begin!")
    st.info("💡 Get your Gemini API Key from: https://aistudio.google.com/app/apikey")