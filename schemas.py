import os
import json


def load(path: str) -> dict:
    """Load a schema file and convert it to dict from your path"""
    schema_path = os.path.join(os.path.dirname(__file__), path)

    with open(schema_path, "r") as schema_file:
        return json.loads(schema_file.read())
