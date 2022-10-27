## https://www.acmicpc.net/source/10601886

def draw_next(lines, shift):
    for i in range(len(lines)):
        lines.append(lines[i]+' '+lines[i])
    for i in range(shift):
        lines[i] = ' '*shift + lines[i] + ' '*shift

def draw_lines(lines):
    print('\n'.join(lines))

def draw_triangle(height):
    lines = ['  *  ',
             ' * * ',
             '*****']

    i = 0
    while height > 3:
        draw_next(lines, 3*(2**i))
        height /= 2
        i+=1

    draw_lines(lines)
    
draw_triangle(int(input()))