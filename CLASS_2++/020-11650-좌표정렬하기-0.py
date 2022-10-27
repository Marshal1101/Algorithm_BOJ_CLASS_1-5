## 18	44061820	3	marshal1101	52648	236	Python 3 / 수정	168

import sys

data = [sys.stdin.readline() for _ in range(int(input()))]
data.sort(key=lambda x: tuple(map(int, x.split())))
print("\n".join(data).replace("\n\n", "\n"))