import streamlit as st
import google.generativeai as genai

# Page set-up
st.set_page_config(page_title="Finder AI", page_icon="🔍")
st.title("🔍 Finder AI")
st.caption("Aapka apna smart assistant")

# 1. API Key Setup (Secrets se link karna)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        # Naya model use kar rahe hain jo fast hai
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Secrets mein GOOGLE_API_KEY nahi mili. Streamlit settings check karein.")
except Exception as e:
    st.error(f"Setup Error: {e}")

# 2. Chat UI
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Finder se kuch bhi puchiye...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"AI Error: {e}")
