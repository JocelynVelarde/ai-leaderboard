
from openai import OpenAI
import streamlit as st

def generate_openai(prompt, api_key):
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="davinci-002",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

