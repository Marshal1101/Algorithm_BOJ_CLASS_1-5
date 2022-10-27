import sys
from bisect import bisect_left


def main():
    input = sys.stdin.readline
    N = int(input())
    nums = [(0, 0)] * (N+1)
    dp = [0] * (N+1)
    cp = [(0, 0)]
    for i in range(N):
        A, B = map(int, input().split())
        nums[i+1] = (B, A)
    
    nums.sort(key=lambda x: x[1])
    # print(nums)
    
    for i in range(1, N+1):
        if nums[i][0] > cp[-1][0]:
            cp.append(nums[i])
            dp[i] = len(cp)-1
        else:
            dp[i] = bisect_left(cp, nums[i])
            cp[dp[i]] = nums[i]
    print(N+1 - len(cp))
    
    max_idx, ans = max(dp), []
    for i in range(N, 0, -1):
        if dp[i] != max_idx:
            ans.append(nums[i][1])
        else: max_idx = dp[i] - 1
    for i in range(len(ans)-1, -1, -1):
        print(ans[i])

if __name__ == '__main__':
    main()