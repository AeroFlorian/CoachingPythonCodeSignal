from utils import check_solution


# After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different
# cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are
# quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.
#
# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to
# return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear
# below a 0).

# First solution
# We use two loops,one on rows, one on columns
# We keep track of all columns that have been haunted

def matrix_elements_sum(matrix):
    res = 0
    haunted = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                haunted.append(j)
            if j not in haunted:
                res = res + matrix[i][j]
    return res


# Second solution
# We can use two loops, but loop on columns and stop when we reach a zero
def matrix_elements_sum_quicker(matrix):
    res = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            if matrix[i][j] == 0:
                # if we reach a haunted room, go to next column
                break
            res += matrix[i][j]
    return res


if __name__ == "__main__":
    super_long_matrix = [[x + 1 for x in range(1000)] for y in range(1000)]
    for x in range(1000):
        super_long_matrix[x][x] = 0

    params = [
        [[[[0, 1, 1, 2],
           [0, 5, 0, 0],
           [2, 0, 3, 3]]], 9],
        [[super_long_matrix], 333333000]
    ]

    check_solution(matrix_elements_sum, params)
    check_solution(matrix_elements_sum_quicker, params)
    # With this input, solution 2 is 50 times quicker than solution 1
