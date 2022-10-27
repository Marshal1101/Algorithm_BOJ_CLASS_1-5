import sys

N = int(sys.stdin.readline())

def check666(num) :
    string = list(str(num))
    conseq_six = 0
    for char in string :
        if char == '6' :
            conseq_six += 1
            if conseq_six == 3 :
                return True
        else :
            conseq_six = 0
    return False

k = 1
s = 666
while k < N :
    s += 1
    if check666(s) :
        k += 1

print(s)