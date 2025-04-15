# Define a Query Refinement Tool (Agent Tool)
# query_refiner.py

def refine_query(query: str) -> str:
    # Simple rule-based refiner; you can replace with LLM if needed
    if "contract" not in query.lower():
        return "Contract related question: " + query
    return query
