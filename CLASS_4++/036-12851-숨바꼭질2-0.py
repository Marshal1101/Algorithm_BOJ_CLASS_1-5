## https://www.acmicpc.net/source/44970274 // joonion

def dfs(n, k):
    if n >= k:
        return n - k, 1
    elif k == 1: # n == 0
        return 1, 1
    elif k % 2 == 0: # k is even
        opt, case = dfs(n, k // 2)
        if k - n == 1 + opt:
            return k - n, case + 1
        elif k - n < 1 + opt:
            return k - n, 1
        else:
            return 1 + opt, case
    else: # k is odd
        opt1, case1 = dfs(n, k + 1)
        opt2, case2 = dfs(n, k - 1)
        if opt1 == opt2:
            return 1 + opt1, case1 + case2
        elif opt1 < opt2:
            return 1 + opt1, case1
        else:
            return 1 + opt2, case2
    
n, k = map(int, input().split())
opt, cnt = dfs(n, k)
print(opt)
print(cnt)