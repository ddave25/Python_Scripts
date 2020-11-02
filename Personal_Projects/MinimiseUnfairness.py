# Using greedy algorithm to get the minimum unfairness from the subarray of an array
# Unfairness = maximum element of subarray - minimum element of subarray

def maxMin(k, arr):

    # Sort all elements in ascending order
    arr.sort()

    # Set minimum difference to largest element allowed in array used to store user inputs
    min_diff = 1000000000

    for i in range(len(arr) - k + 1):
        min_diff = min(min_diff, arr[i + k - 1] - arr[i])

    return min_diff


# Get inputs for size of array and size of subarray
n = int(input())
k = int(input())

# Array to hold all entries
arr = []

# To store all entered user integers in array
for i in range(n):
    arr.append(int(input()))

result = maxMin(k, arr)

print(result)
