from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore



# pdf_path = Path(__file__).parent / "The Ultimate HTML handbook.pdf"
pdf_path = Path(__file__).parent / "The Ultimate Python handbook.pdf"

# Load this file in the python program
loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()  #each docs is 1 page here

# print(docs[0])

# split the docs into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks = text_splitter.split_documents(documents=docs)

# vector embeddings using HuggingFace (Free, runs locally, no API needed)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = QdrantVectorStore.from_documents(
    documents=chunks,   
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

print("indexing of document done...")