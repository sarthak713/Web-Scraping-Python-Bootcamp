# Dictionaries
    # mutable and unordered containers
    # built using { } & key-value pairs
    # values are accessed using [] or .get()
    # adding & removing elements: dict[key]=value, dict.pop(key)

scores={'Andrew':98,'Jess':80,'Sarthak':90}
print(type(scores))

print(scores['Jess'])
print(scores['Sarthak'])
print(scores.get('Andrew'))

# print(scores['Andy'])     # Error
print(scores.get('Andy'))   # None

scores['Tom']=77
print(scores['Tom'])

print(scores)

scores.pop('Tom')
print(scores)