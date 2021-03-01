#lets make  box printer
'''

*******
*     *
*     *
*******

'''
#something like that where you can specify the symbol, height, and width

#lets use the raise and exception statements in order to easily trace custom errors


def boxprinter(symbol, height, width):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be exactly one character') #this will return a custom error statement for this custom error you determined
    if (height < 2 ) or (width < 2):
        raise Exception('"width" or "height" must be greater than 2')
    print(symbol * width)

    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)

    print(symbol * width)

    

boxprinter('*', 7, 8)
