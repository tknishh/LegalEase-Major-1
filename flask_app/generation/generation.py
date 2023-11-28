from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
import textract
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

load_dotenv()
from PIL import Image

# img = Image.open(r"streamlit_apps\understanding\logo.png")
st.set_page_config(page_title="LegalEase: Generate with Ease")
st.header("LegalEase: Generate with Ease📄")
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

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )  

    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    query = st.text_input("Ask you question")
    if query:
        docs = knowledge_base.similarity_search(query)

        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=query)
           
        st.success(response)


# import os
# import time
# from dotenv import load_dotenv
# import pinecone
# from PyPDF2 import PdfReader
# from langchain.embeddings.openai import OpenAIEmbeddings

# load_dotenv()

# data_dir = "data/"
# index_name = "legalease-nda"

# # Connect to Pinecone
# pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENV'))
# embeddings = OpenAIEmbeddings()
# index = pinecone.Index(index_name)

# # Wait a moment for the index to be fully initialized
# time.sleep(1)

# # List PDF files in the data directory
# pdf_files = [file for file in os.listdir(data_dir) if file.endswith(".pdf")]

# # Extract text from multiple PDF files, embed it, and upload the vectors to Pinecone
# for pdf_file in pdf_files:
#     pdf_path = os.path.join(data_dir, pdf_file)

#     # Load the text from the PDF file
#     pdf_reader = PdfReader(pdf_path)
#     text = ""
#     for page in pdf_reader.pages:
#         text += page.extract_text()

#     # Encode the text into vectors using OpenAIEmbeddings
#     vectors = embeddings.embed_query(text)  # Embed the text into vectors

#     # Add the encoded vectors to the Pinecone index
#     pinecone.Index(index_name).upsert(ids=[pdf_file], vectors=vectors)

