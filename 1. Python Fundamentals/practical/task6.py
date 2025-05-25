# Generators and Iterators

# Write a generator function that generates the first 10 even numbers.

# def generateEven():
#     evens = []
#     num = 0
#     count = 0
#     while count < 10:
#         evens.append(num)
#         num += 2
#         count += 1
#     return evens

# print(generateEven())


# ======================================================================


# Write a Python program that uses a custom iterator to iterate over a list of integers.


numbers = [10, 20, 30, 40, 50]

iterator = (i for i in numbers)


for item in iterator:
    print(item)