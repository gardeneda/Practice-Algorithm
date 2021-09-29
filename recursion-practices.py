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


 3. Find the GCD (Greatest Common Divisor) of two numbers using recursion.

# Planning Stage:

# The function is given numbers, and we have to find the biggest numbers that divide each of them

def GCD_iter(x, y):
    pass

def find_GCD(x: int, y: int) -> int:
    """Takes two inputs and finds the greatest common divisor.

    Args:
        x ([int]): Integer 1
        y ([int]): Integer 2

    Returns:
        int: The greatest common divisor of the two given integers
    """
    assert int(x) == x and int(y) == y, "The given numbers should be an integer."
    if x < 0:
        x *= -1
    elif y < 0:
        y *= -1
    elif x % y == 0:
        return y
    else:
        return find_GCD(y, x % y)

(print(find_GCD(8, 12)))
(print(find_GCD(48, 18)))
(print(find_GCD(-81, 72)))
(print(find_GCD(12, -10)))




# 4. Convert a number from Decimal to Binary using recursion.

# Planning Stage:

# What dictates the end of the program?
#   - If n is 0


def dec_to_bin(n: int) -> int:
    assert n >= 0 and int(n) == n, "Given integer should be a positive number. Two's Complement is not reproducible here."
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * dec_to_bin(int(n/2))

print(dec_to_bin(10))
print(dec_to_bin(19999))
