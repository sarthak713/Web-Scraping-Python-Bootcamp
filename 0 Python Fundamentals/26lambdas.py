# Lambda Functions
    # lambdas are functions that don't have a name, they're anonymous
    # lambdas are great for doing one thing in one place
    # they contain only one statement & automatically return the result of that statement

# lambda parameter: return

lambda x: x**2  

a=10
square=lambda x:x**2    # use by giving it a name, but the point of lambda func being anonymous is defeated
print(square(a))

numbers=[10,2,3,1,5,19,82]
print(list(map(square,numbers)))    # map takes a func and a list

print(list(map(lambda x:x**2, numbers)))    # instead of giving it a normal func we give it lambda func