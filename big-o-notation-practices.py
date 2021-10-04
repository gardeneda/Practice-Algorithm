# 1:

def foo(array):
    sum = 0 # O(1)
    product = 1 # O(1)

    for i in array: # O(n)
        sum += i # O(1)

    for i in array: # O(n)
        product *= i # O(1)
    print(f"Sum = {sum}, Product = {product}")  # O(1)

    # O(n), because of dominance.


# 2:

def printPairs(array):
    for i in array: # O(n^2)
        for j in array: # O(n)
            print(f"{i}, {j}") # O(1)
    
    # O(n^2), because of dominance


# 3:

def printUnorderedPairs(array):
    for i in range(0, len(array)): 
        for j in range(i+1, len(array)): 
            # 1st -> n-1
            # 2nd -> n-2
            # 3rd -> n-3 . . . 
            # n(n-1)/2
            print(f"{array[i]}, {array[j]}") 

    # n^2/2+n
    # Therefore, O(n^2)

# 4:

def printUnordeeredPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(f"{arrayA[i]}, {arrayB[j]}") # O(1)

    # O(ab)


# 5:

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):  # O(1)
                print(f"{arrayA[i]}, {arrayB[j]}")
    
    # O(ab)

# 6:

def reverse(array):
    for i in range(0, int(len(array)/2)): # O(n/2)
        other = len(array)-i-1   # O(1)
        temp = array[i]          # O(1)
        array[i] = array[other]  # O(1)
        array[other] = temp      # O(1)
    print(array)                 # O(1)


    # O(n)

# 7: Which of the following are equivalent to O(n)? Why?

# a) O(N + P), where P < N/2
    # O(N) is dominant, so O(N)
# b) O(2N)
    # Constants are dropped. Asymptotic analysis. O(N)
# c) O(N + logN)
    # O(N) is dominant, so O(N)
# d) O(N + NlogN)
# e) O(N+M)
    # Need to keep both variables. Not equal to O(N).


# 8:

def factorial(n):                  # M(n)
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)  # M(n-1)

    # O(n)


# 9:

def allFib(n):
    for i in range(n):
        print(f"{i}, {fib(i)}")

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

    # O(2^n)

# 10:

def powersOf2(n):
    if n < 1:
        return 0
    elif n == 1:
        print(1)
        return 1
    else:
        prev = powersOf2(int(n/2))
        curr = prev * 2
        print(curr)
        return curr

    # O(logn)


