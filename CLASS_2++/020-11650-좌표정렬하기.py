import sys

N = int(sys.stdin.readline())
nxy = list(ele.split() for ele in sys.stdin.readlines())
nxy.sort(key=lambda x: (int(x[0]), int(x[1])))
for xy in nxy :
    print((" ").join(xy))