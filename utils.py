from time import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.10f}s')
        return result
    return wrap_func

@timer_func
def check_solution(solution, args):
    print("======================================")
    print(f"{bcolors.HEADER}Checking solution {solution.__name__}{bcolors.ENDC}")
    try:
        for index, k in enumerate(args):
            result = solution(*k[0])
            assert result == k[1], f"Test {index+1}/{len(args)} failed!\n\tsolution{k[0]}\n\t\texpected: {k[1]}\n\t\tresult:  {result}"
            print(f"{bcolors.OKCYAN}Test {index+1}/{len(args)} passed{bcolors.ENDC}!")
    except AssertionError as e:
        print("Code did not pass Tests!")
        print(f"{bcolors.FAIL}{e}{bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}Solution {solution.__name__} passed tests{bcolors.ENDC}!")
    print("======================================")