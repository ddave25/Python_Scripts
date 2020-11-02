import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):

    XORlr = '{0:b}'.format(l ^ r)

    maxXOR = XORlr.replace('0', '1')

    return int(maxXOR, 2)


l = int(input())

r = int(input())

result = maximizingXor(l, r)

print(result)
