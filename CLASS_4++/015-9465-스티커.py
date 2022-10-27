import sys; input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    N = int(input())
    s1 = list(map(int, input().split()))
    s2 = list(map(int, input().split()))

    if N == 1 :
        print(s1[0] if s1[0] > s2[0] else s2[0])
    else :
        s1[1] = s2[0] + s1[1]
        s2[1] = s1[0] + s2[1]

        for i in range(2, N) :
            s1[i] = s2[i-1] + s1[i] if s2[i-1] > s2[i-2] else s2[i-2] + s1[i]
            s2[i] = s1[i-1] + s2[i] if s1[i-1] > s1[i-2] else s1[i-2] + s2[i]
        
        print(s1[N-1] if s1[N-1] > s2[N-1] else s2[N-1])