import streamlit as st
# pip install requests
import requests
# pip install pandas
import pandas as pd
# Create a title
st.title("📈 LLM Leaderboard Playground")

# Add divider
st.divider()

# Add a subheader
st.subheader("View LLM ratings for different models")

api_url = "https://datasets-server.huggingface.co/first-rows?dataset=optimum-benchmark%2Fllm-perf-leaderboard&config=default&split=train"

try:
    response = requests.get(api_url)
    if response.status_code == 200:
        api_data = response.json()
        features = [feature["name"] for feature in api_data["features"]]
        row = [row["row"] for row in api_data["rows"]]
        df = pd.DataFrame(row, columns=features)
        st.subheader("⭐LLM Leaderboard")
        st.dataframe(df)

except Exception as e:
    st.error(e)