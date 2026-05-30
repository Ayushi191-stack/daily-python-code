#THE game () function in a program lets a user play a game an dreturns the score as an integer. you need to read a file 'Hi-score.txt' which is either blank or contains  the previous hi=score. you need to compare the score returned by the game() function with the hi-score and update the hi-score if the score is greater than the hi-score. Finally, you need to write the (updated) hi-score back to the file 'Hi-score.txt'
import random

def game():
    print("Welcome to the game!")
    score = random.randint(1, 62)
    #fetch the hiscore
    with open("hi-score.txt") as f:
        hiscore = f.read()
        if (hiscore != " "):
            hiscore = int(hiscore)
        else:
            hiscore = 0
    print("Your score is: ", score)
    if score > hiscore:
        print("Congratulations! You have the new hi-score!")
        with open("hi-score.txt", "w") as f:
            f.write(str(score))
    return score