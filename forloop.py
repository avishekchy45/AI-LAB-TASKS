sum = 0
for index in range(0,100,2):
    sum += index
print("Sum =", sum)

sum = 0
for index in range(100):
    if(index%2==0):
        sum+=index
print("Sum =", sum)
