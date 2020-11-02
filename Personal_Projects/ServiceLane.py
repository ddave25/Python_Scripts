import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(width, cases):

    max_allowed_widths = []

    for i in range(len(cases)):
        max_allowed_widths.append(min(width[cases[i][0]:cases[i][1]+1]))

    return max_allowed_widths


nt = input().split()

n = int(nt[0])

t = int(nt[1])

width = list(map(int, input().rstrip().split()))

cases = []

for _ in range(t):
    cases.append(list(map(int, input().rstrip().split())))

result = serviceLane(width, cases)

print(result)
