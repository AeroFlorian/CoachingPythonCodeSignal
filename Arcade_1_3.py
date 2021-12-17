from utils import check_solution


# Given the string, check if it is a palindrome.

# First solution can be to iterate through letters from the right and the left at the same time
# and check if they are equal
def check_palindrome_iterate(input):
    for x in range(len(input) // 2):
        # /!\ first element from the left is 0, first from the right is -1
        if input[x] != input[-1 - x]:
            return False
    return True


# Second solution is to reverse the whole string and compare them
def check_palindrome_reverse(input):
    return input == input[::-1]


if __name__ == "__main__":
    params = [
        [["aabaa"], True],
        [["abac"], False],
        [["a"], True],
        [["az"], False],
        [["abacaba"], True],
        [["z"], True],
        [["aaabaaaa"], False]
    ]

    check_solution(check_palindrome_iterate, params)
    check_solution(check_palindrome_reverse, params)
