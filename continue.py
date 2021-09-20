n = int(input())
sum = 0
for index in range(n):
    if(index % 2 == 0):
        continue
    sum += index
print("Sum =", sum)
