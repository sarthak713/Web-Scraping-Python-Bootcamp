# Lists VS Strings
    # strings are sequence of characters
    # lists are sequence of any object
    # both are ordered
    # Lists are mutable, strings are immutable

py="python"
print(type(py))

students=["boy","girl","gender"]
print(type(students))

print(py[0])
print(students[0])

print(py[0:4])
print(students[0:2])

print(py[-1])
print(students[-1])

# once a string is created, it cannot be changed

print(py)
py="newWords"   # No Error: making py point to a new object & destroying the first one
# py[0]='a'     # Error

print(students)
students[0]="sarthak"
print(students)