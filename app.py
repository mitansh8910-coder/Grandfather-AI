import streamlit as st
from gtts import gTTS
import os
import ollama

# Page Config
st.set_page_config(page_title="Baatein with Dadu", page_icon="👴")

st.title("Yaadein - Baatein with Dadu")
st.image("image_ab5c6b.jpg", caption="Dadu", width=300)

# Initialize Session State for history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input (Voice/Text)
if prompt := st.chat_input("Dadu se kuch bolo..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call the Brain
    with st.chat_message("assistant"):
        response = ollama.chat(model='DaduAI', messages=[{'role': 'user', 'content': prompt}])
        full_response = response['message']['content']
        st.markdown(full_response)
        
        # Create Audio Response
        tts = gTTS(text=full_response, lang='hi')
        tts.save("response.mp3")
        st.audio("response.mp3")

    st.session_state.messages.append({"role": "assistant", "content": full_response})
