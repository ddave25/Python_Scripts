# Start with a 1-indexed array of zeros and a list of operations.
# For each operation, add a value to each of the array element between two given indices, inclusive.
# Once all operations have been performed, return the maximum value in your array.

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    arr = [0 for _ in range(n + 1)]

    for query in queries:

        a = query[0] - 1
        b = query[1]
        k = query[2]

        arr[a] += k
        arr[b] -= k

        print(arr)

    max_value = 0
    sum = 0

    for i in arr:
        sum += i
        if sum > max_value:
            max_value = sum

    return max_value


# The first line contains two space-separated integers, n and m, the size of the array and the number of operations.
nm = input().split()
n = int(nm[0])
m = int(nm[1])

# Each of the next lines contains three space-separated integers, a, b and k, the left index, right index and summand.
queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))

result = arrayManipulation(n, queries)

print(result)
