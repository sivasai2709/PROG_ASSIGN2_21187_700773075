from backend.db import run_query
from backend.llm import natural_to_cypher

def execute_nl_query(natural_text):
    cypher = natural_to_cypher(natural_text)
    result = run_query(cypher)
    return {"cypher": cypher, "result": result}

# CRUD helpers

def create_node(label, props):
    query = f"CREATE (n:{label} $props) RETURN n"
    return run_query(query, {"props": props})

def get_all(label):
    query = f"MATCH (n:{label}) RETURN n"
    return run_query(query)

def update_node(label, name, props):
    query = f"""
    MATCH (n:{label} {{name: $name}})
    SET n += $props
    RETURN n
    """
    return run_query(query, {"name": name, "props": props})

def delete_node(label, name):
    query = f"""
    MATCH (n:{label} {{name: $name}})
    DELETE n
    RETURN 'deleted' as status
    """
    return run_query(query, {"name": name})
