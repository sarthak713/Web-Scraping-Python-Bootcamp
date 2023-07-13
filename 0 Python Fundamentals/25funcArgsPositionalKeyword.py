# Functional Arguments: Postional VS Keywords

# Q1: define a function that formats a name from 'Mary Anderson' to 'Anderson, Mary'

def reverse_name(first,last):   # parameters
    return "{}, {}".format(last,first)

name='Sarthak Bhardwaj'
print(name)
name=reverse_name('Sarthak','Bhardwaj')     # positional arguments = function is relying on their position to assign them with correct parameters
print(name)
name=reverse_name(first='Sarthak',last='Bhardwaj')      # keyword arguments   
print(name)
name=reverse_name(last='Sarthak',first='Bhardwaj')      # keyword arguments   
print(name)
name=reverse_name('Sarthak',last='Bhardwaj')      # mixed arguments - first positional then keyword 
print(name)