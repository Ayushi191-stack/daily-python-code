#find missing number in list
l1 = [1,2,3,5]

n = len(l1) + 1

expected_sum = n*(n +1) // 2
actual_sum = sum(l1)

missing = expected_sum - actual_sum

print("Missing number:", missing)