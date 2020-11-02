#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the flippingBits function below.
def flippingBits(n):

    return int(bin(~n & 0xffffffff), 2)


q = int(input())

for q_itr in range(q):
    n = int(input())

    result = flippingBits(n)

    print(result)
