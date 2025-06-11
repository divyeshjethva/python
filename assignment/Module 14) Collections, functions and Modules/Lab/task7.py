# 7. Working with Dictionaries

# student = {
#     "name": "divyesh",
#     "age": 20,
#     "course": "BCA"
# }

# student["age"] = 21

# print(student)

# =======================================

keys = ["name", "age", "city"]
values = ["Ravi", 25, "Delhi"]

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print("Merged Dictionary:", d)
