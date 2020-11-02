#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np

# Complete the minimumBribes function below.
def minimumBribes(q):

    bribe = 0

    k = [q[i] for i in range(len(q))]
    k.sort()

    ongoing = True

    for i in range(len(q)):

        if q[i] - (i+1) > 2:
            print("Too chaotic")
            return

    while ongoing:
        for i in reversed(range(1, len(q))):
            if q[i] - (i+1) == 0:
                continue
            elif q[i] < q[i-1]:
                q[i], q[i-1] = q[i-1], q[i]
                bribe += 1

                if i == 1 and q != k:
                    break
                elif q == k:
                    ongoing = False
                    break

    print(bribe)
    return

t = int(input())

for t_itr in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimumBribes(q)
