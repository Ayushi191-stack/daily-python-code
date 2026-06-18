#Remove duplicate values
numbers = [1,2,2,3,4,4,5]
unique_numbers = list(set(numbers)) #set() may change order of elements
print(unique_numbers)
#so use
numbers = [1,2,2,3,4,4,5]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)#set remove duplicate numbers and list put it in a list
print(unique_numbers)
