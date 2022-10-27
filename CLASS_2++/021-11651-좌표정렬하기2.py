import sys

data = [sys.stdin.readline() for _ in range(int(input()))]
data.sort(key=lambda x: (int(x.split()[1]), int(x.split()[0])))
print("\n".join(data).replace("\n\n", "\n"))