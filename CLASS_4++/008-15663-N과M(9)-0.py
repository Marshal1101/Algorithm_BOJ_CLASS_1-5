## https://www.acmicpc.net/source/17456423

import sys
input = sys.stdin.readline
print = sys.stdout.write

n,m = map(int,input().split())
arr = input().split()
arr.sort(key=lambda x:int(x))

chk = [False]*n
nums = [0]*m

def DFS(depth=0,n=n,m=m,arr=arr):
    if depth == m:
            print(" ".join(nums)+"\n")
    else:
        before = -1
        for i in range(n):
            if (not chk[i]) & ((i==0) | (before != arr[i])):
                before = arr[i]
                nums[depth]=arr[i]
                chk[i] = True
                DFS(depth+1)
                chk[i]=False

DFS()