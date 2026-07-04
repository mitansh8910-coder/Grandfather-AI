import streamlit as st
import google.generativeai as genai

# Configure your Google Gemini API Key
# You can get a free key at https://aistudio.google.com/
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GOOGLE_API_KEY)

st.title("Yaadein - Baatein with Dadu")

# Display the photo - ensure this matches your file name in GitHub
try:
    st.image("grandfather_face.jpg", caption="Dadu", width=300)
except Exception:
    st.warning("Photo not found. Check if 'grandfather_face.jpg' is in the root folder.")

# Initialize the model
model = genai.GenerativeModel('gemini-pro')

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Talk to Dadu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = model.generate_content(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
