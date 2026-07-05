import streamlit as st
import google.generativeai as genai

# You'll add your API key securely later
st.title("Yaadein - Baatein with Dadu")

# Display the photo (make sure the file is in your folder)
try:
    st.image("grandfather_face.jpg", caption="Dadu", width=300)
except:
    st.write("Photo not found.")

# Simple chat logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Talk to Dadu..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Here you would add the AI response logic later
    with st.chat_message("assistant"):
        st.markdown("This is where Dadu would respond.")
