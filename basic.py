name = "grok"
age = 25
score = [20, 30, 50]
user = {"name": "grok", "age": 25}

print(f"hello, {name}! avg score: {sum(score)/len(score)}")
print(f"hello, {user['name']}! avg score: {sum(score)/len(score)}")