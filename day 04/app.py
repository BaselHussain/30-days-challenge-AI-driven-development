# app.py
import streamlit as st
from agents import Runner
from agent import academic_assistant_agent
from tools import extract_pdf_text  # We still import it for consistency, but we won't use it

st.title("PDF Study Notes Summarizer & Quiz Generator")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # 1. Extract text OURSELVES using pypdf (no agent needed for this)
    with st.spinner("Extracting text from PDF..."):
        pdf_bytes = uploaded_file.read()
        full_text = extract_pdf_text(pdf_bytes)  # ← Just call it directly
    
    st.success(f"Extracted {len(full_text):,} characters from PDF")
    
    # Store in session so both buttons use same text
    st.session_state.full_text = full_text

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Generate Summary", use_container_width=True):
            with st.spinner("Generating summary..."):
                result = Runner.run_sync(
                    academic_assistant_agent,
                    f"Summarize this document clearly and concisely:\n\n{st.session_state.full_text}"
                )
                st.markdown("### Summary")
                st.write(result.final_output)

    with col2:
        if st.button("Create Quiz", use_container_width=True):
            with st.spinner("Creating quiz..."):
                result = Runner.run_sync(
                    academic_assistant_agent,
                    f"Using ONLY the original text below, create a quiz with 10-15 questions "
                    f"(mix of MCQs with 4 options, True/False, Fill-in-the-blank). "
                    f"Hide answers. Number the questions.\n\nText:\n{st.session_state.full_text}"
                )
                st.markdown("### Quiz")
                st.write(result.final_output)