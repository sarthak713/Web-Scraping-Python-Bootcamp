# List Methods & Functions
    # built-in functions: max,len,min,sorted
    # methods:
        # append() to add items to list, returns nothin
        # pop() to remove by index, returns popped element
        # remove() to remove by item
        # str.join(list) to join all elements of list into a string

nums=[20,19,1,8,12.1,12.5]

print(max(nums))
print(min(nums))
print(len(nums))
print(sorted(nums))
print(sorted(nums,reverse=True))

print(nums)
nums.append(24)
print(nums)
nums.pop(-1)
print(nums)
nums.remove(12.5)
print(nums)

students=['age','height','date','name']
print(''.join(students))
print('-'.join(students))