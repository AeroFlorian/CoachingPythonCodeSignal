import math
from utils import check_solution


# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# First solution can be to have a reference and iterate through elements
def adjacent_elements_product(input_array):
    reference = -math.inf
    for i in range(len(input_array)-1): #iterating until the previous to last element
        if input_array[i]*input_array[i+1] > reference:
            reference = input_array[i]*input_array[i+1]
    return reference


# Second solution with list comprehension
# We first use a list storing all products
# and then apply max on it
def adjacent_elements_product_lc(input_array):
    return max([input_array[i]*input_array[i+1] for i in range(len(input_array) -1)])


if __name__ == "__main__":
    super_long_array = [x for x in range(-1000000, 1000000)]
    params = [
        [[[3, 6, -2, -5, 7, 3]], 21],
        [[[-1, -2]], 2],
        [[[5, 1, 2, 3, 1, 4]], 6],
        [[[1, 2, 3, 0]], 6],
        [[[9, 5, 10, 2, 24, -1, -48]], 50],
        [[[5, 6, -4, 2, 3, 2, -23]], 30],
        [[[-23, 4, -3, 8, -12]], -12],
        [[super_long_array], 999999000000]
    ]

    check_solution(adjacent_elements_product, params)
    check_solution(adjacent_elements_product_lc, params)
    # We can see here that using a list and max on it is twice longer
