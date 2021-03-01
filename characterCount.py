message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

#since the message variable is a string, its counted as list-like so the for loop will take it one letter at a time

#upper method would convert everything to uppercase so lower and upper case wont be counted separately
for character in message.upper():  # first would be for 'I' in message
    count.setdefault(character, 0)
    count[character]+= 1


print(count)
#this just makes your output more organized

