# If, Else, Elif
    # if statements allow us to control flow of a program
    # else and elif keywords
    # combining boolean expressions with and,or
    # pitfall: using the assignment '=' operator instead of comparison '=='

passed=[]
failed=[]

student_1={'name':'Jes','score':72,'attend':True}
student_2={'name':'Bri','score':90,'attend':True}
student_3={'name':'May','score':64,'attend':False}

if student_1.get('score')>70:
    passed.append(student_1)

if student_2.get('score')>70:
    passed.append(student_2)
else:
    failed.append(student_2)

print(passed)

if student_3.get('score')>70:
    passed.append(student_3)
elif student_3.get('score')>65 and student_3.get('attend')==True:
    passed.append(student_3)
else:
    failed.append(student_3)

print(failed)

# Indentation is Very Important