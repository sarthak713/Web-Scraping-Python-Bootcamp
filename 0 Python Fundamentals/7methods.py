# Methods
    # similar to functions
    # Example: type()
    # but they are always attached to a type of object
    # different data types have different methods defined & available
    # some methods on strings: upper(), lower(), isalpha(), startsWith()
    
print('python'.upper())
print('HellOWORLD'.lower())
print('pythonv3.9'.isalpha())
print('pythON'.startswith('py'))
print('pythON'.endswith('on'))

# Value Substitution with .format()

print("We will be using python v{} from now".format(3.9))
print("My name is {} boy".format("Sarthak"))

print("We will use python v{py_v}, pandas v{pa_v}, numpy v{nu_v}".format(py_v=3.9, nu_v=1.21, pa_v=7.07))