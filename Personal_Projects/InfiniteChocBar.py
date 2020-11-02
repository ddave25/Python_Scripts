#!/bin/python3

import os
import sys
import math

#
# Complete the halloweenParty function below.
#
def halloweenParty(k):
    #
    # Write your code here.
    #
    if k % 2 == 0:
        return (math.floor(k/2))**2
    else:
        return (math.floor(k/2))*(math.ceil(k/2))


t = int(input())

for t_itr in range(t):
    k = int(input())

    result = halloweenParty(k)

    print(result)
