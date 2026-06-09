numbers = [1,2,2,3,4,4,5]
unique = list(set(numbers))

print(unique)
# it may differ the sequence of numbers

#or
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)