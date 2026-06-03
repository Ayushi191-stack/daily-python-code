import random
n = random.randint(1, 100)
guesses = 0
a = -1
while(a != n):
    a = int(input("guess the number: "))
    
    if a < n:
        print("guess the higher number")
        guesses += 1
    elif a > n:
        print("guess the lower number")
        guesses += 1

print(f"you guessed the number in {guesses} guesses")