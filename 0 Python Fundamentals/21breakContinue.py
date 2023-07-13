# break & continue
    # break exits out of the loop
    # continue skips a single iteration

i=1

for i in range(10):
    if i%2==0:
        continue
    elif i==7:
        break
    else:
        print(i)