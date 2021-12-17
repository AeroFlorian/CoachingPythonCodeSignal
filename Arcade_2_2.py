from utils import check_solution


# Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.
# A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the
# n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3-
# and 4-interesting polygons in the picture below.

# First solution
# We have a two triangles of area 1..3..2*n-1
# Plus one line of length 2*n -1 to remove
# complexity O(n)
def shape_area(n):
    res = 0
    for i in range(1, 2*n, 2):
        res+=2*i
    return res - (2*n -1)


# Second solution
# We realize that solution(n) = solution(n-1) + 4(n-1)
# We can use recursion!!
# Issue with stack length pretty fast
def shape_area_recursive(n):
    if n == 1:
        return 1
    return 4*(n-1) + shape_area_recursive(n-1)

# Third and best solution
# if solution(n) = 4*(n-1) + solution(n-1)
# so solution(n) = 4*(n-1)+4*(n-2)+...+1 = 4*(n-1)*n/2 +1 = 2*n*(n-1) +1
# complexity O(1)
def shape_area_math(n):
    return 2*n*(n-1) +1


if __name__ == "__main__":
    params = [
        [[2], 5],
        [[3], 13],
        [[1], 1],
        [[5], 41],
        [[7000], 97986001],
        [[8000], 127984001],
        [[9999], 199940005],
        [[99999999], 19999999400000005]

    ]

    check_solution(shape_area, params)
    try:
        check_solution(shape_area_recursive, params)
    except RecursionError:
        print("Recursion Limit for > 1000 times")
    check_solution(shape_area_math, params)
