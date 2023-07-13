# Truth Value of Non-Booleans
    # all objects (not just booleans) in python have a truth value
    # falsy objects: None, False, (), {}, [], 0, 0.0

if True:
    print('it is true')
elif False:
    print('it is false')
else:
    print('it is nothin')

if not 77:
    print('True it is')
else:
    print('False it is')