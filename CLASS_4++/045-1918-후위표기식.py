import sys; input = sys.stdin.readline
from collections import deque

def main() :
    infix = deque(list(input().rstrip()))
    print(postfix(infix, False))

def postfix(infix, is_mul) :
    p_pm = ['+', '-']
    p_md = ['*', '/']
    bracket = ['(', ')']

    num = deque([])
    p = deque([])

    while infix :
        i = infix[0]

        if i in p_pm :
            
            if p and is_mul :
                fix = ''.join(num) + ''.join(p)
                # print('p ismul:', fix)
                return fix
            elif p :
                fix = ''.join(num) + ''.join(p)
                num.clear(); p.clear()
                num.append(fix)
            p.appendleft(i)
            infix.popleft()
            
        elif i in p_md :
            if not is_mul :
                infix.appendleft(num.pop())
                num.append(postfix(infix, True))
            else :
                fix = ''.join(num) + ''.join(p)
                num.clear(); p.clear()
                num.append(fix)
                p.appendleft(i)
                infix.popleft()
                # print('mul fix:', num, i, is_mul)
                
        elif i == bracket[0] :
            infix.popleft()
            num.append(postfix(infix, False))
        elif i == bracket[1] :
            fix = ''.join(num) + ''.join(p)
            if is_mul : 
                return fix
            else :
                infix.popleft()
                # print('bracRet:', fix)
                return fix
        
        else :
            num.append(i)
            infix.popleft()

    
    fix = ''.join(num) + ''.join(p)
    # print('nor ret:', fix, 'is_mul:', is_mul, i)
    return fix


if __name__ == '__main__' :
    main()