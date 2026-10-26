"""
Day 173: CSV Write and Read

Question:
Write rows to a CSV file and read them as dictionaries.
"""

# Solution
import csv, os, tempfile

path = os.path.join(tempfile.gettempdir(), "demo.csv")
rows = [{"name": "Ana", "marks": 88}, {"name": "Ben", "marks": 92}]
with open(path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "marks"])
    w.writeheader()
    w.writerows(rows)

with open(path) as f:
    for row in csv.DictReader(f):
        print(row)
os.remove(path)
