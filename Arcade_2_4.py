from utils import check_solution
import math


# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence
# by removing no more than one element from the array.
# Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing
# only one element is also considered to be strictly increasing.

# First solution
# We iterate until we have an issue
# Then we remove the two indexes and try on the new lists
# if one of them is okay, then True, else False
# lets use a function to check if the sequence is increasing
def is_sequence_increasing(sequence):
    prev = -math.inf
    for x in sequence:
        if x <= prev:
            return False
        prev = x
    return True

def almost_increasing_sequence(sequence):
    index_issue = -1
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            index_issue = i
            break
    if index_issue == -1:
        return True
    #/!\ we need to copy the lists here, otherwise
    # as list is mutable, if we do
    # list1 = list2
    # and we modify list1, that will modify list2
    # 2 ways to copy:
    # list1 = list2.copy()
    # or with slicing: list1 = list2[:]
    try1 = sequence[:]
    try1.pop(index_issue)
    try2 = sequence.copy()
    try2.pop(index_issue + 1)
    return is_sequence_increasing(try1) or is_sequence_increasing(try2)


# Second solution
# We can do it in one pass
def almost_increasing_sequence_one_pass(sequence):
    dropped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if dropped:
                # if we already had one issue, so returning False
                return False
            else:
                #dropping one
                dropped = True
            if elm <= prev:
                #means we are jumping over
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
        #okay, move on to the next
            prev, last = last, elm
    return True



if __name__ == "__main__":
    super_long_list = [x for x in range(10000000)] +[9999] +[9998]
    params = [
        [[[1, 3, 2, 1]], False],
        [[[1, 3, 2]], True],
        [[[1, 2, 1, 2]], False],
        [[[3, 5, 67, 98, 3]], True],
        [[[123, -17, -5, 1, 2, 3, 12, 43, 45]], True],
        [[super_long_list], False]
    ]

    check_solution(almost_increasing_sequence, params)
    check_solution(almost_increasing_sequence_one_pass, params)
    #We can see that we are 4 times faster in one pass
