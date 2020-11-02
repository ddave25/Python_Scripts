import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):

    temp = n
    count = 0

    while temp > 0:
        d = temp % 10

        if d > 0 and n % d == 0:
            count += 1

        temp = (temp - d) / 10

    return count


t = int(input())

for t_itr in range(t):
    n = int(input())
    result = findDigits(n)
    print(result)
