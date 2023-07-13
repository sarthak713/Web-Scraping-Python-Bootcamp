# Defining Functions
    # functions allow us to simplify and speed up code by organizing it around reusable blocks
    # functions are great for generalizing repetitive tasks

scores=[90,73,43,100]
print(sum(scores)/len(scores))

def get_average(scores_list):
    return sum(scores_list)/len(scores_list)

print(get_average(scores))


# Q1: add an average score to each student dictionary in students list

students=[
    {'name':'boy','score':[90,73,43,90]},
    {'name':'cat','score':[76,44,66,73]}
]
print(students)

def add_average(students):
    for i in students:
        sum=0
        number=0
        for score in i.get('score'):
            number+=1
            sum+=score
        i['average']=sum/number

add_average(students)
print(students)


# second way
students2=[
    {'name':'boy','score':[90,73,43,90]},
    {'name':'cat','score':[76,44,66,73]}
]

def add_average2(students):
    for i in students:
        i['average']=get_average(i.get('score'))
        if i.get('average')>70:
            i['passed']=True
        else:
            i['passed']=False

add_average2(students2)
print(students2)