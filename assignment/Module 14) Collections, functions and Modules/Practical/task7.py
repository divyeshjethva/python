
# person = {
#     "name": "Anjali",
#     "age": 22,
#     "city": "Pune"
# }

# person["city"] = "Mumbai"

# print(person)

# =================================================

# student = {
#     "name": "rohan",
#     "grade": "A",
#     "marks": 85
# }

# keys = student.keys()
# values = student.values()

# print("keys:", list(keys))
# print("values:", list(values))

# =================================================

# keys = ["id", "name", "subject"]
# values = [101, "divyesh", "Maths"]

# result = {}

# for i in range(len(keys)):
#     result[keys[i]] = values[i]

# print(result)

# =================================================


text = "programming"

d = {}

for i in text:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print("Character Frequency:")
for char, count in d.items():
    print(char,":",count)
