def eggs(randomParameter):
    randomParameter.append('Hello')

spam = ['1','2','3']
eggs(spam)
print(spam)


# if you run this module you'll see that 'Hello' was appended to spam :+{
# this doesnt follow the earlier lessons on scope since we learned that the local scope of the function eggs should not apply to global scope
# the explanation here is that the reference if of the list assigned to spam gets copied to the randomParameter
