# Dictionaries Keys & Values
    # values could be any other value or container object, even other dictionaries
    # keys could be any immutable data type
    # keys(), values(), items()

scores={
    'Andrew': {
        'name':'boy',
        'age':30
    },
    'Jess': [80,96,56], 
    'Sarthak': True
}

print(scores)

sample={7: [10,20,'Sarthak'], ('Tom','Jerry'): True}
print(sample)

# sampleSet={['name','age']:5}    # Error, list as key is immutable

sampleDict={'name':89,'age':20,'gender':0}
print(sampleDict.keys())
print(sampleDict.values())
print(sampleDict.items())

print(type(sampleDict.keys()))
print(type(sampleDict.values()))
print(type(sampleDict.items()))