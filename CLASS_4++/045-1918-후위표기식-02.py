## https://www.acmicpc.net/source/30746094

# 1918번
import sys
input=sys.stdin.readline

priority = {'*':3,'/':3,'+':2,'-':2,'(':1}
op = []
res=[]
s=input().rstrip()

for i in s:
    if i == '(':
        op.append(i)
    elif i in '+-*/':
        while op and priority[op[-1]]>=priority[i]:
            res.append(op.pop())
        op.append(i)
    elif i == ')':
        while op and op[-1]!='(':
            res.append(op.pop())
        op.pop()
    else:
        res.append(i)

while op:
    res.append(op.pop())

print(''.join(res))