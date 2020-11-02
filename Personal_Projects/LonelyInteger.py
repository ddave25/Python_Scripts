def lonelyinteger(a):
    result = a[0]

    # XOR all elements in array
    # 2 equal elements will cancel out each other when XOR-ed
    # Remainder will be unique integer
    for i in range(1, len(a)):
        result ^= a[i]

    return result


n = int(input())

a = list(map(int, input().rstrip().split()))

result = lonelyinteger(a)

print(result)
