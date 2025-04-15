# Main App
# a multi-agent RAG system that reads PDF contracts and answers legal questions
# main.py

from pdf_loader import load_and_split_pdf
from embedding_store import init_vector_store
from rag_chain import build_rag_chain
from agent_setup import create_agent

if __name__ == "__main__":
    file_path = "contracts/nda_contract.pdf"  # your local path
    docs = load_and_split_pdf(file_path)
    vector_store = init_vector_store(docs)
    
    rag_chain = build_rag_chain(vector_store)
    agent = create_agent(rag_chain)
    
    while True:
        query = input("Ask a legal question: ")
        if query.lower() in ["exit", "quit"]:
            break
        print(agent.run(query))
