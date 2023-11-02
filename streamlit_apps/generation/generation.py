import pinecone
import os
import numpy as np
from dotenv import load_dotenv

data_dir = "data/NDA/"
index_name = "legalease-nda"

# Connect to Pinecone
pinecone.init(api_key='PINECONE_API_KEY', environment='PINECONE_ENV')

# Get all files in data_dir
files = os.listdir(data_dir)
print(files)

# Iterate over files and add them to the index
for file in files:
	# Load the data from the file
	data = np.load(os.path.join(data_dir, file))
	
	# Encode the data using a vector encoder
	encoder = pinecone.Index(index_name).vector_encoder()
	vectors = encoder.encode(data)
	
	# Add the encoded vectors to the index
	pinecone.Index(index_name).upsert(vectors)

# Disconnect from Pinecone
pinecone.deinit()

