s = {1,6,86,86,1,6} #sets are unordered collection of unique items
print(s) # it will give omly 1time 1 as sets didnt give repeated value

#methods of set
s.add(100) # to add an element in the set
print(s, type(s))

s1= {1,6,86,86,1,6}
s2 = {7,87,6,1,89,100}
print(s1.union(s2)) # will give us the union of two sets
print(s1.intersection(s2)) # will give us the intersection of two sets