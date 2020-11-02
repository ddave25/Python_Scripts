#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):

    arr = re.findall('[a-zA-Z][^A-Z]*', s)

    return len(arr)


s = input()

result = camelcase(s)

print(result)
