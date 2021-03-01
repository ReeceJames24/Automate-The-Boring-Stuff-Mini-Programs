spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('Spam is ' + str(spam))

# the continue here tells the program to loop back to the start of while block once the varibale equals 3 so it skips the print call.
