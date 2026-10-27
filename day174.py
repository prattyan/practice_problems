"""
Day 174: JSON Dump and Load

Question:
Convert a dictionary to JSON and back.
"""

# Solution
import json

data = {"name": "Neha", "skills": ["Python", "SQL"], "age": 24}
s = json.dumps(data, indent=2)
print(s)
print(json.loads(s)["skills"])
