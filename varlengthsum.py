def add(*n):
    sum = 0
    for i in n:
        sum += i
    return sum
print(add(1, 2, 3, 4))
print ("\n")
def add2(*n):
    for i in n:
        print(i)
add2(1, 2)
