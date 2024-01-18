# This is a guess the number game.
import random

print ('Hello. what is your name')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20')
sN = random.randint(1, 20)

for guessT in range(1, 7):
    print('Take a gusss')
    guess = int(input())

    if guess < sN:
        print('Your guess is too low')
    elif guess > sN:
        print('Your guess is too high')
    else:
        break# is if correct guess!


if guess == sN:
    print('Good job, ' + name + ' You guessed in ' + str(guessT) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(guessT))
stop = input()
