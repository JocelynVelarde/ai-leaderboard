import streamlit as st

st.title("➡️ Welcome to the LLM Playground")

st.divider()

model = st.selectbox("Select a model", ["GPT-4", "GPT-3.5", "Gemini", "BERT"])
st.write(f"You selected {model}")

user_prompt = st.chat_input("Enter your prompt")

if st.button("Send"):
    # Perform LLM function calls
    st.success("Generating response")
else:
    st.warning("Please fill out with a prompt")