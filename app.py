import streamlit as st
from sentiment import predict_sentiment

st.set_page_config(
    page_title="Twitter Sentiment Analyzer",
    page_icon="🐦",
    layout="centered"
)

st.title("Twitter Sentiment Analysis")

text = st.text_area(
    "Enter a tweet:",
    placeholder="Type or paste a tweet here...",
    height=120
)

SENTIMENT_UI = {
    "Positive": {"emoji": "😄", "type": "success"},
    "Neutral":  {"emoji": "😐", "type": "info"},
    "Negative": {"emoji": "😡", "type": "error"},
}

if st.button("Analyze"):
    if not text.strip():
        st.warning("Please enter a tweet first.")
    else:
        label, _ = predict_sentiment(text)

        ui = SENTIMENT_UI[label]
        message = f"{ui['emoji']}  **{label}**"

        if ui["type"] == "success":
            st.success(message)
        elif ui["type"] == "info":
            st.info(message)
        elif ui["type"] == "error":
            st.error(message)
