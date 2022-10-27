import sys


input = sys.stdin.readline

N = int(input())
M = int(input())
words = list(input().strip())

count = 0
I_cnt = 0
is_turn_for_I = True
for char in words :
    if I_cnt > 0 :
        if char == 'O' :
            if is_turn_for_I == False :
                is_turn_for_I = True
            else : 
                if I_cnt > N :
                    count += I_cnt - N
                I_cnt = 0
        else :
            if is_turn_for_I :
                I_cnt += 1
            else :
                if I_cnt > N :
                    count += I_cnt - N
                I_cnt = 1
            is_turn_for_I = False
    
    else :
        if char == 'I' :
            I_cnt = 1
            is_turn_for_I = False

if I_cnt > N :
    count += I_cnt - N
print(count)