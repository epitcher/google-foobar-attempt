import math
import functools

# The grandest staircase

def doCache(func):
    c = {}
    @functools.wraps(func)
    def store(arg):
        if arg not in c:
            c[arg] = func(arg)
        return c[arg]

    return store


@doCache
def sum_odd_factors(N):
    n = float(N)

    return sum([
        i if n / i == i else i + n / i
        for i in range(1, int(math.sqrt(n) + 1)) if n % i == 0
    ])


@doCache
def permutations(n):
    if n == 0 or n == 1: return 1

    def s(n):
        if n % 1 == 0:
            return sum_odd_factors(n)
        else:
            return 0

    answer = sum([
        (s(k) - 2 * s(k / 2.0)) * permutations(n - k)
        for k in range(1, n + 1)
    ])

    answer /= n

    return int(answer)


def solution(n):
    return permutations(n) - 1



print(solution(200))
# Expect 487067745

print(solution(3))
# Expect 1
