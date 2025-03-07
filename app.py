import streamlit as st
from llm_abstraction import LLMHandler

st.title("Multi-Functional AI Assistant")
user_input = st.text_input("Enter your query:")

if st.button("Submit"):
    llm = LLMHandler()
    llm.load_model("gpt2")
    response = llm.generate_text(f"Please provide a detailed explanation of {user_input}.")
    st.write(response)
