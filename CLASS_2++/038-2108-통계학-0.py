## https://www.acmicpc.net/source/30150156

from sys import stdin


def sol2108():
    n = int(stdin.readline())
    counts = [0]*8001
    s = 0
    for i in stdin:
        num = int(i)
        counts[num+4000] += 1

    maxc = max(counts)
    mode = mcnt = 0
    idx = 0
    med = None
    mi, ma = 4001, -4001
    for i in range(8001):
        cnt = counts[i]
        if cnt == 0:
            continue

        num = i-4000
        s += num*counts[i]
        if cnt == maxc and mcnt < 2:
            mode = num
            mcnt += 1
        mi = min(mi, num)
        ma = max(ma, num)
        idx += counts[i]
        if idx >= n//2+1 and med == None:
            med = num

    print(round(s/n), med, mode, ma-mi, sep='\n')


if __name__ == '__main__':
    sol2108()