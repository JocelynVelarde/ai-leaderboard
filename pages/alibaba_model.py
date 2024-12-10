import streamlit as st
from algorithms.alibaba import generate_alibaba 

st.title("➡️ Welcome to the Alibaba Cloud Model Playground")

st.subheader("This model is powered by Alibaba Cloud using the Qwen/QwQ-32B-Preview model from the Hugging Face Hub.")

st.divider()

model = st.selectbox("Select a model", ["Qwen/QwQ-32B-Preview"])
st.write(f"You selected {model}")

user_prompt = st.text_input("Write your message")
response = generate_alibaba(user_prompt)
st.write(response)