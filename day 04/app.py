import streamlit as st
from agents import Runner
from agent import academic_assistant_agent

st.title("PDF Study Notes Summarizer & Quiz Generator")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    file_bytes = uploaded_file.read()

    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            result = Runner.run_sync(
                academic_assistant_agent,
                f"Please summarize the following text:\n\n{file_bytes}",
            )
            st.write(result.final_output)

    if st.button("Create Quiz"):
        with st.spinner("Creating quiz..."):
            result = Runner.run_sync(
                academic_assistant_agent,
                f"Please create a quiz from the following text:\n\n{file_bytes}",
            )
            st.success(result.final_output)