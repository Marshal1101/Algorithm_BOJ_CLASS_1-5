import sys
from bisect import bisect_right

def prime_list(n) :
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m+1) :
        if sieve[i] == True :
            for j in range(i+i, n+1, i) :
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i] == True]


def sequential_count(primes: list, N) :
    if N == 1 : return 0
    count = 0
    if primes[-1] == N :
        count += 1
    
    max_len = primes_len if (primes_len := len(primes)) < 10000 else 10000
    for seq_len in range(2, max_len) :
        idx = bisect_right(primes, N//seq_len)
        zero_idx_flag = False
        sum = 0
        if idx >= seq_len - 1 :
            for j in range(seq_len) :
                sum += primes[idx-j]
        else :
            for j in range(seq_len) :
                sum += primes[j]
                zero_idx_flag = True
                
        if sum == N : 
            count += 1
        elif sum > N :
            if zero_idx_flag : return count
            else : continue
        else :
            if zero_idx_flag :
                rp = seq_len
                lp = 0
            else :
                rp = idx + 1
                lp = idx - (seq_len-1)
            while sum < N and rp < primes_len :
                sum -= primes[lp]
                sum += primes[rp]
                lp += 1
                rp += 1
            if sum == N :
                count += 1

    return count


def main() :
    N = int(sys.stdin.readline())
    primes = prime_list(N)
    cnt = sequential_count(primes, N)
    print(cnt)

if __name__ == '__main__' :
    main()