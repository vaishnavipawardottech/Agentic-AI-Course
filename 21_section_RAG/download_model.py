from sentence_transformers import SentenceTransformer

# This will download the model with retries
print("Downloading model...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
print("Model downloaded successfully!")
