import sys

input = sys.stdin.readline

def solution() :
    N = int(input())
    res = ''
    stack = []
    ptr = 0
    i = 0
    while (i <= N) :
        try : num = int(input())
        except : break
        # print(i, num)
        while (i < num) :
            i += 1
            stack.append(i)
            ptr += 1
            res += '+\n'
        if num == stack[ptr-1] :
            stack.pop()
            ptr -= 1
            res += '-\n'
        else :
            return 'NO'
        # print('end', i)
    return res

print(solution())
