# 🧠 Agentic RAG Legal Assistant

This project implements an **Agentic Retrieval-Augmented Generation (RAG)** system using **LangChain**, **OpenAI GPT-4**, and **Pinecone** to intelligently answer legal questions from PDF contracts. It demonstrates how to build a modular, agent-driven pipeline for domain-specific question answering.

---

## 🚀 Features

- 📄 **PDF Ingestion & Chunking**: Loads and splits large documents for processing.
- 🧬 **Embeddings + Vector Search**: Stores contract content in Pinecone using OpenAI embeddings.
- 🤖 **RAG QA Chain**: Uses retrieved chunks to generate context-aware answers.
- 🦾 **Query Refinement Agent**: Dynamically improves vague or general user questions.
- 💬 **Conversational Memory** (Optional): Maintains context during multi-turn interactions.
- 🔁 **Modular Architecture**: Each component is a separate script for flexibility.

---

## 🛠 Project Structure

```bash
agentic-rag-legal/
│
├── pdf_loader.py           # Loads and splits PDF documents
├── embedding_store.py      # Generates embeddings and stores in Pinecone
├── rag_chain.py            # Sets up the RAG retrieval chain
├── query_refiner.py        # Simple refinement tool for vague queries
├── agent_setup.py          # Defines and initializes the agent
├── memory_support.py       # Optional memory management for context
├── main.py                 # Entry point for the app
├── contracts/              # Folder for input PDFs (e.g., NDA contracts)
└── .env                    # Environment variables for API keys
