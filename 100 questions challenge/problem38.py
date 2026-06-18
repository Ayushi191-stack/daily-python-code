#set union and inteersection
l1 = [1,2,2,3,3,3,4,4,5]
l2 = [6,6,7,7,7,8,8,9]
merged_list = l1 + l2
unique_numbers = list(set(merged_list))
print(unique_numbers)#union by me

#intersection
l1 = [1,2,2,3,3,3,4,4,5]
l2 = [4,5,2,3,5,6,7,8,9]
intersection = set(l1) & set(l2)
print(intersection)