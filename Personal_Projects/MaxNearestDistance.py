#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):

    c.sort()

    maxd = max(c[0], n-c[-1]-1)

    for i in range(len(c)-1):
        maxd = max((c[i+1]-c[i])//2, maxd)

    return maxd


nm = input().split()

n = int(nm[0])

m = int(nm[1])

c = list(map(int, input().rstrip().split()))

result = flatlandSpaceStations(n, c)

print(str(result) + '\n')


