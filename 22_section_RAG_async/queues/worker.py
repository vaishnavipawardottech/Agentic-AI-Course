import os
from dotenv import load_dotenv
from openai import OpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

# Load environment variables from .env file
load_dotenv()

# vector embeddings using HuggingFace (Free, runs locally, no API needed)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Initialize Gemini client for chat
client = OpenAI(
    api_key=os.getenv("api_key"),  # Load API key from .env file
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)


def process_query(query: str) :
    search_result = vector_db.similarity_search(query=query)

    context = "\n\n\n".join([f"page_content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_result])

    SYSTEM_PROMPT = f""" You are an AI assistant that helps people find information. 
                        Use the context provided to answer the user's question. 
                        If the context does not contain the answer, respond with "I don't know".

                        Context:
                        {context}

                        """

    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",
        messages=[
            {"role": "system", "content":SYSTEM_PROMPT},
            {"role": "user", "content":query}
        ]
    )
    print(f"Response: {response.choices[0].message.content}")
    return response.choices[0].message.content