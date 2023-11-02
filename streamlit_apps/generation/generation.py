import pinecone
import os
import numpy as np
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain import OpenAIEmbeddings, PineconeStore

load_dotenv()

data_dir = "data/"
index_name = "legalease-nda"

# Connect to Pinecone
pinecone.init(api_key=os.getenv('PINECONE_API_KEY'), environment=os.getenv('PINECONE_ENV'))

index = pinecone.Index(index_name)
# wait a moment for the index to be fully initialized
time.sleep(1)

# files
files = os.listdir(data_dir)
print(files)

# Extract text from multiple PDF files in a directory, encode it and push to index
for file in files:
	# Load the data from the file
	pdf_reader = PdfReader(os.path.join(data_dir, file))
	text = ""
	for page in pdf_reader.pages:
		text += page.extract_text()
	
	# Encode the data using a vector encoder
	embeddings = OpenAIEmbeddings()
	PineconeStore.fromDocuments(text, embeddings)
	
	# Add the encoded vectors to the index
	pinecone.Index(index_name).upsert(vectors)

# Disconnect from Pinecone
pinecone.deinit()