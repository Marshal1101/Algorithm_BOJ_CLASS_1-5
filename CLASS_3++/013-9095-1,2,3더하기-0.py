## https://www.acmicpc.net/source/18171622

t = int(input())
arr = [1, 2, 4]
for i in range(3, 10):
    arr.append(arr[i - 3] + arr[i - 2] + arr[i - 1])
for i in range(t):
    n = int(input())
    print(arr[n - 1])