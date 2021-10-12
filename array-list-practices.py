import numpy as np
import random

# 1 How do you find the missing number in an integer array of 1 to 100?

def missingNum_generator(n: int) -> int:
    range_of_value = np.array([num for num in range(1, (n+1))])
    missing = np.delete(range_of_value, (random.randint(1, n)))
    # print(missing) # For testing purposes.
    return missing

def findMissing(array, n: int) -> int:
    sum1 = n*(n+1)/2
    sum2 = sum(array)
    return int(sum1 - sum2)

# print(findMissing(missingNum_generator(100), 100))


# 2 Two Sum


def twoSum(nums: list, target: int) -> list:
    
    # Attempt to solve without using nested for-loops.

    answer = []
    for num in nums:
        index = nums.index(num)
        i = len(nums) - 1
        
    while i != index:
        if num + nums[i] == target:
            solution_num1 = nums.index(num)
            answer.append(solution_num1)
            answer.append(nums.index(nums[i], (solution_num1 + 1)))
            return answer
        i = i -1


def twoSum2(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]




# Using hashmaps could've made this solution much easier.
# But this is array and list practices, so will stick to using solutions in this manner.


# 3 How to check if an array contains a specific number in Python

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def linear_search(array, target):
    """ Finds if the target number is contained within the array.

    Args:
        array [numpy.array]: Array created by numpy.
        target [int]: Wanted integer
    """
    if target in array:
        loc = np.where(myArray == target)
        return loc

print(linear_search(myArray, 9))



# 4 Find the maximum product of two integers in an array with positive integers

Array4 =  np.array([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])

def findMaxProduct(array) -> list:
    """finds the max product that can be achieved with the postiive integers in a one-dimiensional array.

    Args:
        array ([numpy array]): One-dimensional array with positive integers.

    Returns:
        list: Returns the two integers and the maximum product in a list, in order. [n1, n2, max_product]
    """
    max_product = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            product = array[i] * array[j]
            if product > max_product:
                max_product = product
                num1 = array[i]
                num2 = array[j]

    return [num1, num2, max_product]

print(findMaxProduct(Array4))


# The above is a 'brute force' method of doing this. O(n^2) time complexity; so not time efficient.

# A better way to do this is to probably find the two maximum values in the array
# And then to multiply them together.

def findMaxProduct2(Array4):
    first_maxvalue = np.amax(Array4)
    Array4 = Array4[Array4 != first_maxvalue]
    second_maxvalue = np.amax(Array4)
    max_product = first_maxvalue * second_maxvalue

    return [first_maxvalue, second_maxvalue, max_product]

print(f"This is the more optimized version of findMaxProduct: {findMaxProduct2(Array4)}")

# The above follows a time complexity of O(mn), which has a better time complexity than the one above.

