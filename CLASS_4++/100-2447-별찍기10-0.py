n= int(input())

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]

def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    print('x', x, 'n', n)
    top_bottom = concatenate(x, x)
    middle = concatenate(x, [' '*n]*n)
    return top_bottom + middle + top_bottom

print('\n'.join(star10(n)))