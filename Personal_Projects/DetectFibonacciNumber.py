import math


# Complete the solve function below.
def solve(n):

    a = 5*n*n + 4
    b = 5*n*n - 4

    testA = math.sqrt(a)
    testB = math.sqrt(b)

    if testA == math.ceil(testA) or testB == math.ceil(testB):
        return "IsFibo"
    elif testA == math.floor(testA) or testB == math.floor(testB):
        return "IsFibo"
    elif testA == round(testA) or testB == round(testB):
        return "IsFibo"
    else:
        return "IsNotFibo"


t = int(input())

for t_itr in range(t):
    n = int(input())

    result = solve(n)

    print(result)
