import streamlit as st
# pip install requests
import requests
# Create a title
st.title("📈 LLM Leaderboard Playground")

# Add divider
st.divider()

# Add a subheader
st.subheader("View LLM ratings for different models")

api_url = {
    "https://datasets-server.huggingface.co/first-rows?dataset=optimum-benchmark%2Fllm-perf-leaderboard&config=default&split=train"
}

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        api_data = response.json()
        st.write(api_data)
except Exception as e:
    st.error(e)