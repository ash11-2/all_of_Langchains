# Generate Embeddings and Store in VectorDB (Pinecone)
# embedding_store.py

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone
import os

def init_vector_store(documents):
    embeddings = OpenAIEmbeddings()

    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment="us-west1-gcp")
    
    return Pinecone.from_documents(
        documents,
        embeddings,
        index_name="legal-docs-index"
    )
