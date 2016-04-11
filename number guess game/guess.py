from random import randint
from math import floor

input1="0 20"
input2="13 52"
bonus="0 200"

def guess(inp, player=True):
    minn,maxn = map(int,inp.split())
    mynum = randint(minn,maxn)
    print "Guess a number between %d and %d."%(minn, maxn)
    if player:
        playersearch(minn,maxn,mynum)
    else:
        compsearch(minn,maxn,mynum)    

def playersearch(minimum, maximum, number):
    guesses = 0
    while True:
        try:
            guess = int(raw_input("> "))
            while guess<minimum or guess>maximum:
                print "Try between %d and %d."%(minimum,maximum)
                guess = int(raw_input("> "))
        except ValueError:
            guess=minimum-1
            print "Not a valid number."
            continue
        guesses+=1
        if guess > number: print "Your guess is higher."
        elif guess < number: print "Your guess is lower."
        elif guess == number: 
            print "You got it correct after %d guesses."%guesses
            return 

def compsearch(minimum, maximum, number):
    left, right = minimum, maximum
    guess = floor((left+right)/2)
    steps = 1
    print "Computer guesses %d."%guess
    while guess!=number:
        if guess < number:
            print "Your guess of %d is lower."%guess
            left = guess+1
        elif guess > number:
            print "Your number of %d is higher."%guess
            right = guess-1
        guess = floor((left+right)/2)
        steps+=1

    print "Number %d found in %d guesses."%(guess,steps)


if __name__ == "__main__":
    guess(input1)
    guess(input2)
    guess(bonus)
    print "-----CPUs turn-----"
    guess(input1,False)
    guess(input2,False)
    guess(bonus,False)
