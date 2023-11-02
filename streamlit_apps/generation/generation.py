import os
import time
from dotenv import load_dotenv
import pinecone
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings

load_dotenv()

data_dir = "data/"
index_name = "legalease-nda"

# Connect to Pinecone
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENV'))
embeddings = OpenAIEmbeddings()
index = pinecone.Index(index_name)

# Wait a moment for the index to be fully initialized
time.sleep(1)

# List PDF files in the data directory
pdf_files = [file for file in os.listdir(data_dir) if file.endswith(".pdf")]

# Extract text from multiple PDF files, embed it, and upload the vectors to Pinecone
for pdf_file in pdf_files:
    pdf_path = os.path.join(data_dir, pdf_file)

    # Load the text from the PDF file
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # Encode the text into vectors using OpenAIEmbeddings
    vectors = embeddings.embed_query(text)  # Embed the text into vectors

    # Add the encoded vectors to the Pinecone index
    pinecone.Index(index_name).upsert(ids=[pdf_file], vectors=vectors)


# Query the index
query = "This Agreement is made and entered into as of the Effective Date by and between"
vectors = embeddings.embed_query(query)
results = index.query(queries=vectors, top_k=5)

# Print the results
print("Query:", query)
for result in results[0].results:
	print(result.id, result.score)


