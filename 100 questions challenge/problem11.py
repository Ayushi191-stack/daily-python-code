#count vowels
word = "education"
count = 0  #it means count from 0 of every character og word
for ch in word.lower():  #ch means every  characters of word
    if ch in "aeiou":
        count += 1

print("Number of vowels:", count)