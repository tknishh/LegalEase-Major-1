import streamlit as st
import textract
from PyPDF2 import PdfReader


def upload_new_template():
    # Function to handle uploading new template
    st.write("Upload new template functionality goes here")

def work_with_existing_template(template):
    # Function to handle working with existing template
    st.write(f"Working with existing template: {template}")

def generate_app():
    st.title("LegalEase")

    # Add a heading for the "Generation" block
    if st.button("Generation"):
        generation_option = st.radio("Select an option:", ("Upload new template", "Use existing template"))
        if generation_option == "Upload new template":
            upload_new_template()
        elif generation_option == "Use existing template":
            template = st.selectbox("Select a template:", ("NDA", "Master Agreement", "Evaluation Agreement"))
            work_with_existing_template(template)

    # Add a heading for the "Understanding" block
    if st.button("Understanding"):
        file = st.file_uploader("Upload your file")
        if file is not None:
            content = file.read()  # Read the file content once

            if file.type == 'application/pdf':
                pdf_reader = PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
            elif file.type == 'text/plain':
                text = content.decode('utf-8')
            elif file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                text = textract.process(content)

            query = st.text_input("Ask your question")
            if query:
                # Process the query and provide the answer
                st.write(f"Processing query: {query}")

if __name__ == "__main__":
    generate_app()
