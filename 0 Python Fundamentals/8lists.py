# LISTS
    # lists are ordered sequences of elements
    # denoted with []
    # each element has an index, first starting at 0 (zero-based indexing)
    # we select items from lists using the respective index
    # ...or sequence of indices (list slicing)
    # slicing rules
        # lower bound is inclusive, upper bound is exclusive
        # can also select from end using negative indexing system
        # if we get out of bounds, python throws Indexerror

students=["Andrew","Tristan","Matrix"]
print(students[1])
print(students[0])

print(students[0:3])

print(students[-1]) # last element
print(students[-2])
