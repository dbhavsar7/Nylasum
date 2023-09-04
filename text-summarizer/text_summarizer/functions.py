import openai
import streamlit as st

def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]