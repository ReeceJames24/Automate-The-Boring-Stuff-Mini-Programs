#Input Validation Example

print('How many cats do you own?')
numCats = input()
try:
    if int(numCats) >= 5:
        print('You have a ton of cats man')
    elif int(numCats) < 0:
        print('Negative cats??!')
    else:
        print("That ain't much cats man")

except:
    print('Please input a digit')

#the except clause here allows you to print out a string instead of showing the ugly value error whenever someone inputs a non-digit answer
    
    
