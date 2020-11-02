import math


# Complete the counterGame function below.
def counterGame(n):

    count = 0

    while n != 1:

        test = n != 0 and ((n & (n - 1)) == 0)

        if test == 1:
            n = math.floor(n/2)
            print(n)

        else:
            n = n - 2**math.floor(math.log2(n))
            print(n)

        count = count + 1

    if count % 2 != 0:
        return "Louise"
    else:
        return "Richard"


t = int(input())

for t_itr in range(t):
    n = int(input())

    result = counterGame(n)

    print(result)
