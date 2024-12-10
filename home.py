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

        # Two level filter
        st.subheader("Filter Data")
        selected_col = st.selectbox("Select the column to filter", df.columns)
        unique_values = df[selected_col].dropna().unique()
        selected_vals = st.selectbox(f"Select a value {selected_col}", unique_values)
        filtered_data = df[df[selected_col] == selected_vals]
        st.dataframe(filtered_data)

        # Visualize information in graph format
        st.subheader("Some nice graphs for LLM performance")
        metric = st.selectbox("Select a performance to view", [
            "Average", "IFEval", "BBH"
        ])
        if metric in df.columns:
            st.bar_chart(df[[metric, 'Model']].set_index("Model").sort_values(metric, ascending=False))

except Exception as e:
    st.error(e)