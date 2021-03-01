#guess the number game

import random
print('Hi! What is your name?')
username=input()
print('Well ' + username + ', I am thinking of a number between 1 and 20. Make a guess!')
secretNumber = random.randint(1,20)
#ask the player to guess 6 times
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = input()
    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else: 
        break #this breaks the loops prematurely before they reach the 6th guess assumign they guess the number correctly by then
if guess == secretNumber:
    print('Congrats! You guessed my number in ' + str(guessesTaken) + ( 'guesses. What a smart lad aintcha.')

          
        
