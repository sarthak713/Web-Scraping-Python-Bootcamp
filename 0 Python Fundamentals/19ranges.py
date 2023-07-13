# Range
    # range() is an immutable sequence type that is very useful in for loops
    # ...start, stop, and step must be integers

# range(start,stop,step)

print(range(3,10,2))
print(type(range(3,10,2)))

print(list(range(3,10,1)))
print(list(range(0,11,2)))

for i in range(3):  # with single argument, start is taken as 0, stop is the argument
    print('hi')

print(list(range(5)))
print(list(range(0,5)))

