import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of Program')
def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1): #+ 1 since we want to include the end of the range
        total *= i
        logging.debug('i is %s and total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total
        
    
print('The factorial of 5 is:')
print(factorial(5))

logging.debug('End of program')

#the logging.debug will allow us to see each line of code and its output while it runs per step so we can spot the errors easily
