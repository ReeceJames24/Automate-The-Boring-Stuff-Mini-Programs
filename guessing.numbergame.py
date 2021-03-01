#guess the number game
print('Hello! What is your name?')
name = input()
import random
secretNumber = random.randint(1,20)
print('Well, ' + str(name) + ', I am thinking of a number between 1 and 20')

#guessing time
for guessesTaken in range(1,7):
    print('Take a guess')
    guess = int(input())
    if guess > secretNumber:
        print('Too high')
    elif guess < secretNumber:
        print('too low')
    else:
        break

if guess == secretNumber:
    print('Nice! You got the number in ' + str(guessesTaken) + ' try/tries!')


else:
    print('Sorry, the number i was thinking of was ' + str(secretNumber))
    




    
