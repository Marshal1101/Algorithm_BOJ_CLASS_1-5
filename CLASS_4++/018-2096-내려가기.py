import sys; input = sys.stdin.readline

N = int(input())
max_pre1, max_pre2, max_pre3 = 0, 0, 0
min_pre1, min_pre2, min_pre3 = 0, 0, 0
for i in range(N) :
    num1, num2, num3 = map(int, input().split())

    temp1 = max_pre1 + num1 if max_pre1 > max_pre2 else max_pre2 + num1
    temp2 = max(max_pre1, max_pre2, max_pre3) + num2
    temp3 = max_pre3 + num3 if max_pre3 > max_pre2 else max_pre2 + num3
    max_pre1, max_pre2, max_pre3 = temp1, temp2, temp3

    temp1 = min_pre1 + num1 if min_pre1 < min_pre2 else min_pre2 + num1
    temp2 = min(min_pre1, min_pre2, min_pre3) + num2
    temp3 = min_pre3 + num3 if min_pre3 < min_pre2 else min_pre2 + num3
    min_pre1, min_pre2, min_pre3 = temp1, temp2, temp3

print(max(max_pre1, max_pre2, max_pre3), end=" ")
print(min(min_pre1, min_pre2, min_pre3))