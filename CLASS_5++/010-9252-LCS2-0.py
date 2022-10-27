## https://www.acmicpc.net/source/44424215

s1 = input()
s2 = input()

dp = []
for c in s2:
    prv = '', -1
    for i, cur in enumerate(dp):
        for j in range(prv[1]+1, cur[1]):
            if s1[j] == c:
                dp[i] = (prv[0]+c, j)
                break
        prv = cur
    for j in range(prv[1] + 1, len(s1)):
        if s1[j] == c:
            dp.append((prv[0]+c, j))
            break

if dp:
    print(len(dp))
    print(dp[-1][0])
else:
    print(0)