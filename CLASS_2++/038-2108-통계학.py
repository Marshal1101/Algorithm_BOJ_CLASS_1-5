import sys

input = sys.stdin.readlines()

N = int(input[0])
arr = list(map(int, input[1:]))
# print(N)
# print(arr)
count = {}
max_cnt = 0
max_list = []
for num in arr :
    # print(count)
    # print(num)
    try : 
        count[num] += 1
    except :
        count[num] = 1
    if count[num] > max_cnt :
        max_cnt = count[num]
        max_list.clear()
        max_list.append(num)
    elif count[num] == max_cnt :
        max_list.append(num)
arr.sort()
max_list.sort()
# print('answer')
print(round(sum(arr) / N))
print(arr[N//2])
print(max_list[1]) if len(max_list) > 1 else print(max_list[0])
print(max(arr) - min(arr))