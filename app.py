import streamlit as st
from transformers import pipeline

# Load your fine-tuned model
summarizer = pipeline("summarization", model="shakespeare_summarizer_final", tokenizer="shakespeare_summarizer_final")

st.title("Archaic Text Summarizer 📝")
st.subheader("Convert old English to modern summaries")

input_text = st.text_area("Enter archaic text here:")

if st.button("Summarize"):
    if input_text.strip():
        summary = summarizer(input_text, max_length=100, min_length=30, do_sample=False)
        st.success("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("Please enter some text.")
