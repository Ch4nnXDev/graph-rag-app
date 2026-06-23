from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI", "bolt://localhost:7687"),
            auth=(os.getenv("NEO4J_USER", "neo4j"), os.getenv("NEO4J_PASSWORD", "password"))
        )

    def close(self):
        self.driver.close()

    def run_query(self, query, params=None):
        with self.driver.session() as session:
            result = session.run(query, params or {})
            return [r.data() for r in result]

neo4j_client = Neo4jClient()
