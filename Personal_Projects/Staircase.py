import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):

    for i in range(1, n+1):
        output = ''
        space = n - i

        while space > 0:
            output += ' '
            space -= 1

        for j in range(i):
            output += '#'

        print(output)

n = int(input())

staircase(n)