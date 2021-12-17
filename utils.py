def check_solution(solution, args):
    try:
        for index, k in enumerate(args):
            result = solution(*k[0])
            assert result == k[1], f"Test {index+1}/{len(args)} failed!\n\tsolution{k[0]}\n\t\texpected: {k[1]}\n\t\tresult:  {result}"
            print(f"Test {index+1}/{len(args)} passed!")
    except AssertionError as e:
        print("Code did not pass Tests!")
        print(f"{e}")
    else:
        print("Code passed tests!")