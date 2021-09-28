#1. Find the sum of the digits of a positive integer number using recursion.

def find_sum(n):
    n = str(n)
    list = []
    x = 0
    for char in n:
        list.append(char)
    for num in list:
        x += int(num)
    return (x)

# If I didn't use recursion, the above example would be how I do it.

def recursion_findsum(n: int) -> int:
    assert n >= 0, "Number should be a positive number"
    if n < 10:
        return n
    elif n == 10:
        return n/10
    else:
        return int(n%10) + recursion_findsum(int(n/10))    

# print(find_sum(12665))
# print(find_sum(90))
# print(find_sum(57))
# print(recursion_findsum(12665))
# print(recursion_findsum(90))
# print(recursion_findsum(57))


#2. Calculate the power of a number using recursion.


# Planning Stage:

# We're not using **, the exp. (that defeats the purpose of the q.)
# exp == the number of n * n we have to perform

# What does the function have to return to create a recursive?
#   - I know I need to call a function (power_of_number(n, exp-1))

# What should I do if the base number is negative?
#   - 

# CONSTRAINT: (exp) should not be 0. 

def power_of_number(n: int, exp: int, sign: int) -> int:
    """Takes number and multiplies it by itself (exp) many times.
    Essentially finds the power of a number.

    Args:
        n (int): Base number
        exp (int): The exponent number
        sign (int): -1 if given base number is a negative integer, if not 1

    Returns:
        int: the power (exp) of base number (n)
    """
    assert exp >= 0 and exp == int(exp), "Can only take positive integers for exponents."
    if exp == 0:
        return 1 * sign
    else:
        return n * power_of_number(n, exp-1, sign)

print(power_of_number(2, 4, 1))
print(power_of_number(2, 4, -1))
