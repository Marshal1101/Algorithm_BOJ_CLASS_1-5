import sys
sys.setrecursionlimit(10**9)

def sudoku(idx, end_idx, zero_yx, metrix, Rv, Cv, Av) :
    si, sj = zero_yx[idx]
    for num in range(1, 10) :
        if (not Rv[si][num] and
            not Cv[sj][num] and
            not Av[(ai := si//3)][(aj := sj//3)][num]
            ) :
            Rv[si][num] = Cv[sj][num] = Av[ai][aj][num] = True
            metrix[si][sj] = num

            if idx == end_idx :
                # print('exit')
                for line in metrix :
                    print(''.join(map(str, line)))
                exit()

            sudoku(idx+1, end_idx, zero_yx, metrix, Rv, Cv, Av)
            
            metrix[si][sj] = 0
            Rv[si][num] = Cv[sj][num] = Av[ai][aj][num] = False



def main() :
    input = sys.stdin.readline
    Rv = [[False] * 10 for _ in range(9)]
    Cv = [[False] * 10 for _ in range(9)]
    Av = [[[False] * 10 for _ in range(3)] for _ in range(3)]

    metrix = []
    zero_yx = []
    for i in range(9) :
        line = list(map(int, input().rstrip()))
        for j in range(9) :
            if (num := line[j]) != 0 :
                Rv[i][num] = True
                Cv[j][num] = True
                Av[i//3][j//3][num] = True
            else : zero_yx.append((i, j))
        metrix.append(line)
    
    end_idx = len(zero_yx) - 1
    sudoku(0, end_idx, zero_yx, metrix, Rv, Cv, Av)


if __name__ == '__main__' :
    main()