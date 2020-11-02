import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):

    ServeTime = []

    for i in range(len(orders)):
        ServeTime.append([orders[i][0] + orders[i][1], i+1])

    order = []

    for i in sorted(ServeTime):
        order.append(i[1])

    return order


n = int(input())

orders = []

for _ in range(n):
    orders.append(list(map(int, input().rstrip().split())))

result = jimOrders(orders)

print(result)
