import sys; input = sys.stdin.readline


def get_chk_cross(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    min_x12, max_x12 = (x1, x2) if x1 < x2 else (x2, x1)
    min_y12, max_y12 = (y1, y2) if y1 < y2 else (y2, y1)
    min_x34, max_x34 = (x3, x4) if x3 < x4 else (x4, x3)
    min_y34, max_y34 = (y3, y4) if y3 < y4 else (y4, y3)

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    # 평행
    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if min_x12 <= max_x34 and min_x34 <= max_x12 and min_y12 <= max_y34 and min_y34 <= max_y12:
            return 1
    # 교차
    else:
        if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
            return 1
    return 0


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def main():
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(get_chk_cross(list1, list2))


if __name__ == '__main__':
    main()