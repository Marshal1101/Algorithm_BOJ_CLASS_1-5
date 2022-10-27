## PyPy3

import sys
input = sys.stdin.readline
n=int(input())
d=[0]*50001
for i in range(1,n+1):
  li=[]
  j=1
  while i>=j**2:
    li.append(d[i-j**2])
    j+=1
  d[i]=min(li)+1
print(d[n])