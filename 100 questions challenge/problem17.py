#check Anagram
#Anagram means take two word which is made up of same alphabets if they ,are call anagram if they not, its not anagram
word1 = input("ENter 1st word:")
word2 = input("Enter 2nd word:")
if sorted(word1.lower()) == sorted(word2.lower()):
    print("it's an Anagram")
else:
    print("it's not")