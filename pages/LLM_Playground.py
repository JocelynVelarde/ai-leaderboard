import streamlit as st
from algorithms.gpt import generate_openai

st.title("➡️ Welcome to the LLM Playground")

st.divider()
api_key = st.text_input("Introduce your API Key to start the chat")

model = st.selectbox("Select a model", ["GPT-4", "GPT-3.5", "Gemini", "BERT"])
st.write(f"You selected {model}")

user_prompt = st.text_input("Write your message")
response = generate_openai(user_prompt, api_key)
st.write(response)