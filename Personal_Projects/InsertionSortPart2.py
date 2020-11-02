# Complete the insertionSort2 function below.
def insertionSort2(n, arr):

    if n == 1:
        print(arr[0])
    else:

        for i in range(1, n):

            j = i

            while j > 0 and arr[j-1] > arr[j]:

                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

                j -= 1

            print(" ".join(str(i) for i in arr[::1]))



n = int(input())

arr = list(map(int, input().rstrip().split()))

insertionSort2(n, arr)
