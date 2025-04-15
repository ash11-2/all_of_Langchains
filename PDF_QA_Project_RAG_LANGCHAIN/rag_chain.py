# Create Retrieval-Augmented QA Chain
# rag_chain.py

from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def build_rag_chain(vector_store):
    llm = ChatOpenAI(model_name="gpt-4")
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_type="similarity", k=5),
        chain_type="stuff"
    )
