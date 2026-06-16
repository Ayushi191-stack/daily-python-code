#Rotate list
lst = [1, 2, 3, 4, 5]
k = 2  # k = position

k = k % len(lst)
lst = lst[k:] + lst[:k]

print(lst)

#or

lst = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter number of rotations: "))

k = k % len(lst)
rotated = lst[-k:] + lst[:-k]

print("Rotated list:", rotated)