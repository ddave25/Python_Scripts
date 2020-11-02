# Problem:
# Given nonnegative integer n, want to find nonnegative integers i, such that
# i. 0 <= i <= n
# ii. n + i = n XOR i

# Complete the sumXor function below.
def sumXor(n):

    # Solution

    # n + i = n XOR i + n AND i
    # want to find i where n AND i = 0
    # Thus, i must be a value which unsets all set bits of n's binary value
    # i.e. i must change all the ones in n to zeros

    # if the kth bit in n=1, the kth bit of i must be 0
    # else the kth bit of i can either be 0 or 1
    # therefore, ttl.no.of values i musttake = 2 ^ (no.of zeros in n)

    if n == 0:
        return 1

    else:

        count = 0

        for i in range(2, len(bin(n))):

            if bin(n)[i] == '0':
                count += 1

        return 2**count


n = int(input().strip())

result = sumXor(n)

print(result)

