
# Write a function that returns the sum of 2 parameters

def add_two_numbers(param1, param2):
    return param1 * param2



if __name__ == "__main__":
    params = [
        [[1,2], 3],
        [[10,20], 30],
        [[-1,-2], -3]
    ]
    from utils import check_solution
    check_solution(add_two_numbers, params)