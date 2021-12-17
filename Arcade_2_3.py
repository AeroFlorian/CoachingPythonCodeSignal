from utils import check_solution


# Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an
# non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest
# so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able
# to accomplish that. Help him figure out the minimum number of additional statues needed.
# All statues are distinct in height

# First solution
# as all statues are distinct height, we can take the min, the max, and
# remove the length
def make_array_consecutive(statues):
    return max(statues) - min(statues) + 1 - len(statues)


# Second solution
# Same as the first, but valid if some statues are the same height
def make_array_consecutive_set(statues):
    statues_set = set(statues)
    return max(statues_set) - min(statues_set) + 1 - len(statues_set)


if __name__ == "__main__":
    params = [
        [[[6, 2, 3, 8]], 3],
        [[[0, 3]], 2],
        [[[5, 4, 6]], 0],
        [[[1]], 0]
    ]

    check_solution(make_array_consecutive, params)
    check_solution(make_array_consecutive_set, params)
