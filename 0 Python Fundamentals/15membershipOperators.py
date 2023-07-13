# Membership Operators
    # efficiently test membership with 'in' and 'not in' operators

scores={'Andrew':98,'Jess':80,'Sarthak':90}
print('Brandon' in scores)
print('Jess' in scores)
print('Sarthak' not in scores)

students=['boy','girl','age','names']
print('age' in students)
print('height' not in students)
print(7 in students)

mySet=89,90,91
print(89 in mySet)

# Behind the scenes python stores strings in list with each character taking us a space

name="Sarthak Bhardwaj"
print('t' in name)
print('B' not in name)