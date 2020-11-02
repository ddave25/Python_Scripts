# Complete the sockMerchant function below.
def sockmerchant(n, ar):

    result = 0

    for i in list(set(ar)):
        result += int(ar.count(i)/2)

    return result


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockmerchant(n, ar)

print(result)
