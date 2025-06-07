import requests
import json
import csv


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

with open("todos.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for t in todos:
        writer.writerow(t)
