## https://www.acmicpc.net/source/39891324

from sys import stdin


input = stdin.readline


def get_prime(n):
    n += 1
    # [ 쓰레기값, 3, 5, 7, 9, 11, 13, ... ] 에 대응됨
    sieve = [True] * (n // 2)
    # 3부터 홀수만 검사 (2를 제외한 모든 소수는 홀수이므로)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            k = i * i
            # k=9 -> sieve[4]=9 / i=3는 소수고 sieve[4::3]=[9, 15, 21,...]은 소수가 아님
            # k=25 -> sieve[14]=25 / i=5는 소수고 sieve[14::5]=[25, 35, 45, ...]은 소수가 아님
            sieve[k // 2::i] = [False] * ((n - k - 1) // (2 * i) + 1)

    return [2] + [2 * i + 1 for i in range(1, len(sieve)) if sieve[i]]


def solve():
    N = int(input())

    if N == 1:
        return 0

    prime = get_prime(N)

    left, _sum, ans = 0, 0, 0
    for right in range(len(prime)):
        _sum += prime[right]

        while _sum > N:
            _sum -= prime[left]
            left += 1

        if _sum == N:
            ans += 1
            _sum -= prime[left]
            left += 1

    return ans


if __name__ == '__main__':
    print(solve())
