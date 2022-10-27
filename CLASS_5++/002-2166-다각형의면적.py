from random import randrange
import sys

def randominput() :
    res = ""
    N = randrange(3, 10)
    for _ in range(N) :
        a, b = map(str, [randrange(-10, 10), randrange(-10, 10)])
        res += a + " " + b + "\n"
    return [N, res]

def main() :
    input = sys.stdin.readline
    N = int(input())
    # N, arr = randominput()
    # input = arr.split("\n")
    xy = []
    for i in range(N) : 
        xy.append(list(map(int, input[i].split())))

    xy.append(xy[0])
    up = 0; down = 0
    for i in range(N) :
        up += xy[i][0] * xy[i+1][1]
        down += xy[i][1] * xy[i+1][0]

    print(round(abs(up - down) / 2, 1))

# def triangle_area(p1: tuple, p2: tuple, p3: tuple) :
#     x1, y1 = p1; x2, y2 = p2; x3, y3, = p3
#     u = x1*y2 + x2*y3 + x3*y1
#     w = y1*x2 + y2*x3 + y3*x1
#     res = abs(u - w) / 2
#     # print(p1, p2, p3, res)
#     return res

if __name__ == '__main__' :
    main()