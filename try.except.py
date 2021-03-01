def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('You tried to divide by 0')
            
print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(16))




#notes:
# the program will encounter an error and crash if you try to divide a number by 0 and all subsequent call functions won't be reached
# in order to prevent that, you use the try and except clauses as used above
# note that if you can remove "ZeroDivisionError" if you want that print call to show for any error encountered not just the zerodivision error
