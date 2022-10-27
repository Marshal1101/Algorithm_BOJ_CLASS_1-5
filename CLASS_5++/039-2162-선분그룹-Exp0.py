## https://www.acmicpc.net/source/13549508

# 2162
import sys


def collide(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    # Step 1
    # check that range of two lines have intersection
    if (x1 if x1 > x2 else x2) < (x3 if x3 < x4 else x4) or (x3 if x3 > x4 else x4) < (x1 if x1 < x2 else x2):
        return False
    if (y1 if y1 > y2 else y2) < (y3 if y3 < y4 else y4) or (y3 if y3 > y4 else y4) < (y1 if y1 < y2 else y2):
        return False
    # Step 2
    # line1 = [x1, y1, x2, y2], line2 = [x3, y3, x4, y4]
    # Linear Equation of line 1 : (y1-y2)X - (x1-x2)Y + (x1*y2 - x2*y1) = 0
    # Matrix Expression of Equations, Ax = b
    # [y2-y1 | -(x2-x1)] [x] = [x1*y2 - x2*y1]
    # [y4-y3 | -(x4-x3)] [y] = [x3*y4 - x4*y3]
    # det A = (x2-x1)*(y4-y3) - (x4-x3)*(y2-y1)
    det = (x2-x1)*(y4-y3) - (x4-x3)*(y2-y1)
    if det != 0:  # two lines are not parallel
        # calculating coordinates of intersection point
        x = ((x2-x1)*(x3*y4-x4*y3) - (x4-x3)*(x1*y2-x2*y1)) / det
        y = ((y2-y1)*(x3*y4-x4*y3) - (y4-y3)*(x1*y2-x2*y1)) / det
        # check that intersection point is in range
        lies_in_range = (x-x1)*(x-x2) <= 0 and (x-x3)*(x-x4) <= 0 and (y-y1)*(y-y2) <= 0 and (y-y3)*(y-y4) <= 0
        return True if lies_in_range else False
    else:  # two lines are parallel
        return True if (y2-y1)*x3 - (x2-x1)*y3 + (x2*y1-x1*y2) == 0 else False
        # (x3, y3) is on line1. Shortly, line1 and line2 are same.
        # Cause of Step1, we do not have to check the range.

n = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nbd_ = [[j for j in range(n) if collide(lines[i], lines[j]) and i!= j] for i in range(n)]

group = []
vertices = set([i for i in range(n)])  # using for operation with neighborhood
visited = [False for i in range(n)]
while vertices:
    tmp_group = set([])
    now = vertices.pop()
    tmp_group.add(now)
    visited[now] = True
    to_go = nbd_[now]
    while to_go:
        now = to_go.pop(0)
        vertices.remove(now)
        tmp_group.add(now)
        visited[now] = True
        for nbd in nbd_[now]:
            if not visited[nbd] and nbd not in to_go:
                to_go.append(nbd)
    group.append(tmp_group)

print(len(group))
print(max([len(i) for i in group]))
