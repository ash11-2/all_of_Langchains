# Set Up Agent with Tools
# agent_setup.py

from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from query_refiner import refine_query

def create_agent(qa_chain):
    llm = ChatOpenAI(model_name="gpt-4")
    
    tools = [
        Tool(
            name="RAGLegalQA",
            func=qa_chain.run,
            description="Answers legal questions based on uploaded contracts"
        ),
        Tool(
            name="Refiner",
            func=refine_query,
            description="Refines vague legal queries"
        )
    ]
    
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )
