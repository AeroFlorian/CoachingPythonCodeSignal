from utils import check_solution

# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100,
# the second - from the year 101 up to and including the year 200, etc.

# First solution is to use shift one year to have 1700 in 17th century
def century_from_year(year):
    return (year - 1) // 100 + 1


# Another solution is to check if we have decimals
def century_from_year_decimals(year):
    if year / 100 == year // 100:
        return year // 100
    return year // 100 + 1


if __name__ == "__main__":
    params = [
        [[1905], 20],
        [[1700], 17],
        [[1988], 20],
        [[2000], 20],
        [[2001], 21],
        [[200], 2],
        [[45], 1],
        [[8], 1]
    ]

    check_solution(century_from_year, params)
    check_solution(century_from_year_decimals, params)
