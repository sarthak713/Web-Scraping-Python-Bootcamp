# Zipping Iterables
    # zip creates an iterable (a zip object) combining values from several other iterables
    # values could be unpacked in a for loop

names=['Tom','Jerry','Nobita','Jian','Sunio']
score=[100,90,74,84,70]

print(zip(names,score))
print(list(zip(names,score)))

for i in zip(names,score):
    print(i)

# unpacking tuple
for student_name, student_score in zip(names,score):
    print('{} got a {} on the exam'.format(student_name,student_score))

# can zip as many list as we want