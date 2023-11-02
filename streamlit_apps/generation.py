import pinecone
import os

load_dotenv()
# Connect to Pinecone
pinecone.init(      
	api_key='PINECONE_API_KEY',      
	environment='gcp-starter'      
)

# Create a new index
index_name = "legalease-nda"

# Load the custom dataset
data_dir = "../data/NDA/"
data = np.load(data_path)

# Encode the data using a vector encoder
encoder = pinecone.Index(index_name).vector_encoder()
vectors = encoder.encode(data)

# Add the encoded vectors to the index
pinecone.Index(index_name).upsert(vectors)

# Disconnect from Pinecone
pinecone.deinit()
