#unique elements finder
l1 = [1,2,2,3,3,3,4,4,5]
l2 = [4,5,2,3,5,6,7,8,9]
unique_elements = set(l1) ^ set(l2)
print(unique_elements)