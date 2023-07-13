# List Comprehensions
    # list comprehensions are a pythonic way to build lists, sets, dictionaries without a for loop

# Q1: create a list containing all odd integers in numbers

numbers=[10,2,3,4,17,92,9,33]
odds=[]

# First Way
for num in numbers:
    if num%2!=0:
        odds.append(num)
print(odds)

# Second Way: [element for element in iterable]
odds=[element for element in numbers]   # give back elements as is
odds=[num for num in numbers]           # same
odds=[e**2 for e in numbers]            # square each element in number list
print(odds)

odds=[num for num in numbers if num%2!=0]
print(odds)


# Q2: create a list of all students who scored more than 90

students=[
    {'name':'andrea','score':91},
    {'name':'castix','score':76},
    {'name':'beatri','score':64},
    {'name':'karena','score':96},
]

passed=[student for student in students if student.get('score')>90]
print(passed)
passed=[student for student in students if student['score']>90]
print(passed)

# print only student names
names=[student.get('name') for student in students]
print(names)