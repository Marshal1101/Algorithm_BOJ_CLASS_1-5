## https://www.acmicpc.net/source/17411747

import sys

def main():
    N = int(sys.stdin.readline())
    board = []
    for _ in range(N):
        board.append(sys.stdin.readline())
    
    def check(row,col,l):
        if l==1:
            return board[row][col]
        else:
            half = l//2
            divide = [
                (0,0),(0,half),(half,0),(half,half)
            ]
            now = []
            for x,y in divide:
                now.append(check(row+x,col+y,half))
            l = 1
            for s in now:
                l *= len(s)
            if l==1 and now[0]==now[1]==now[2]==now[3]:
                return now[0]
            return "("+now[0]+now[1]+now[2]+now[3]+")"
    print(check(0,0,N))
main()