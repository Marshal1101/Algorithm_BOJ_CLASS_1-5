## https://www.acmicpc.net/source/25564201

l = input()
S = []
for i in l:
    if i.isalpha(): print(i,end='')
    elif i=='*' or i=='/':
        if S and (S[-1]=='*' or S[-1]=='/'): print(S.pop(), end='')
        S.append(i)
    elif i=='+' or i=='-':
        while True:
            if (not S) or S[-1]=='(': break
            print(S.pop(), end='')
        S.append(i)
    elif i=='(': S.append('(')
    else:
        while S and S[-1]!='(': print(S.pop(),end='')
        S.pop()
while S: print(S.pop(),end='')