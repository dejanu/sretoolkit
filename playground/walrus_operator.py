

# assigment operator for named expression = run a expression while simultaneously assigning the output value to a variable
sample_data = [
    {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False},
    {"userId": 1, "id": 2, "title": "quis ut nam facilis", "completed": False},
    {"userId": 1, "id": 3, "title": "fugiat veniam minus", "completed": False},
    {"userId": 1, "id": 4, "title": "et porro tempora", "completed": True},
    {"userId": 1, "id": 4, "title": None, "completed": True},
]


print("With Python 3.8 Walrus Operator:") 
for entry in sample_data: 
    if title := entry.get("title"):
        print(f'Found title: "{title}"')

print("Without Walrus operator:")
for entry in sample_data:
    title = entry.get("title")
    if title:
        print(f'Found title: "{title}"')
