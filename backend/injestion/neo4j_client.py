from neo4j import GraphDatabase, basic_auth
import os

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv()
        )