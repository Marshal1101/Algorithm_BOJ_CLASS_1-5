import sys

input = sys.stdin.readline
n, m = map(int, input().split())
addr_pwd ={}
for _ in range(n) :
    addr, pwd = input().split()
    addr_pwd[addr] = pwd
for _ in range(m) :
    addr = input().split()[0]
    print(addr_pwd[addr])