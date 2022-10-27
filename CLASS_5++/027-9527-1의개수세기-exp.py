## https://www.acmicpc.net/source/18107800

A, B = map(int, input().split())

def one_cnt(N):
    if N == 0 : return 0
    l = len(str(bin(N)))-3   
    def fullbit(x): return x * 2**(x-1)
    return int(fullbit(l) + N-2**(l)+1 + one_cnt(N-2**(l)))

print(one_cnt(B)-one_cnt(A-1))


## https://www.acmicpc.net/source/14737587

z=r=0
for w in input().split():
 n=int(w)+z;z+=1;i=99;d=2**i
 while n:
  d//=2;i-=1
  if n>=d:n-=d;r-=d*i//2+n
 r=-r
print(r)