#1. How to find the sum of digits of a positive integer number using recursion?

def find_sum(n):
    n = str(n)
    list = []
    x = 0
    for char in n:
        list.append(char)
    for num in list:
        x += int(num)
    return (x)

def recursion_findsum(n):
    assert n >= 0, "Number should be greater than 0"
    if n < 10:
        return n
    elif n == 10:
        return n/10
    else:
        return int(n%10) + recursion_findsum(int(n/10))    

print(recursion_findsum(12665))
print(recursion_findsum(90))
print(recursion_findsum(57))
