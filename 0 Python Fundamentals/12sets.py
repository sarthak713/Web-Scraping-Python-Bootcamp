# SETS
    # unordered container of (only) unique values
    # constructed using { } and comma-separated elements
    # add() & discard() to add and remove values
    # intersection(), difference(), union() 
    # shortcut: remove all duplicates from a list using set()

nums={1,2,2,6,4,5,7,7}
print(nums)
print(type(nums))

# print(nums[0])    # Error

nums.add(10)
nums.add('myself')
print(nums)

nums.discard('myself')
print(nums)

s1={2,3,4,5,6}
s2={4,5,6,7,8}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s2.difference(s1))

# Remove duplicates from list

points=[1,2,3,2,4,4,5,3,1,8,9]
print(type(points))

print(set(points))

points_unique = list(set(points))
print(points_unique)