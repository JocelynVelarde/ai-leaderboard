import streamlit as st
from huggingface_hub import InferenceClient

def generate_alibaba(prompt):

	client = InferenceClient(api_key=st.secrets["hfkey"])

	messages = [
		{
			"role": "user",
			"content": prompt
		}
	]

	completion = client.chat.completions.create(
		model="Qwen/QwQ-32B-Preview", 
		messages=messages, 
		max_tokens=500
	)

	return completion.choices[0].message.content
