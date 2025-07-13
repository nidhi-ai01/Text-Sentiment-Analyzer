# sentiment_app.py

import streamlit as st
from textblob import TextBlob

# App Title
st.title("🧠 Text Sentiment Analyzer")
st.subheader("🔍 Find out whether a sentence is Positive, Negative or Neutral")

# User Input
user_input = st.text_area("✏️ Enter your sentence here")

# Analyze Button
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Sentiment analysis
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        # Result
        if polarity > 0:
            sentiment = "😊 Positive"
        elif polarity < 0:
            sentiment = "😠 Negative"
        else:
            sentiment = "😐 Neutral"

        # Output
        st.success(f"Sentiment: {sentiment}")
        st.info(f"Polarity Score: {polarity:.2f}")
