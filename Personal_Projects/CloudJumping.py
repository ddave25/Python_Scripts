#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    s1 = "".join([str(elem) for elem in c])

    x = s1.split('1')

    jumps = len(x)

    for i in range(len(x)):
        jumps += math.floor(len(x[i])/2)

    return(jumps-1)


n = int(input())

c = list(map(int, input().rstrip().split()))

print(c)

result = jumpingOnClouds(c)

print(str(result) + '\n')

