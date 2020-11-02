import math

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):

    # ar[i] mod k will pair with (k - ar[i] mod k) mod k

    # list to store the count of values ar[i] mod k evaluates to
    modK = []

    for i in range(k):
        modK.append(0)

    # calculate ar[i] mod k and increment the index in modK corresponding to that result
    # i.e. if ar[i] = 1 and k = 3, 1 mod 3 = 1. Thus, modK[1] incremented by 1
    for i in range(n):
        modK[ar[i] % k] += 1

    # variable to count divisible sum pairs
    sum = 0

    # for ar[i] mod k = 0, there will be n*(n-1)/2 pairs
    # n = no. of elements in ar satisfying ar[i] mod k = 0
    sum += math.floor((modK[0] * (modK[0] - 1))/2)

    # if k is even, there will be pairs (ar[i], ar[j]) where ar[i] mod k = ar[j] mod k = k/2
    # there will be n*(n-1)/2 pairs
    # n = no. of elements in ar satisfying ar[i] mod k = k/2
    if k % 2 == 0:
        sum += math.floor((modK[math.floor(k/2)] * (modK[math.floor(k/2)] - 1))/2)

    # for ar[i] mod k = {1, ..., (k-1)}, there will be m * n pairs
    # m = no. of elements satisfying ar[i] mod k = {1, ..., (k-1)}, starting with ar[i] mod k = 1
    # n = no. of elements satisfying (k - ar[i] mod k) mod k to pair with elements counted in m
    # iterate over half the array based on the search algorithm to prevent double counting
    for i in range(1, math.floor(k/2)+1):

        # Skip index i where i = (k-i) as the calculation for these pairs is different
        # this case will only occur if k is even
        if i == (k - i):
            continue
        else:
            sum += (modK[i] * modK[k - i])

    return sum


nk = input().split()

n = int(nk[0])

k = int(nk[1])

ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)

print(result)
