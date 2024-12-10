
from openai import OpenAI
import streamlit as st

def generate_openai(prompt):
    api_key = st.secrets["openai"]
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

