def solution(M, F):
    m, f = int(M), int(F)

    counter = 0
    while not (m == 1 and f == 1):
        if f <= 0 or m <= 0:
            return "impossible"
        if f == 1:
            return str(counter + m - 1)
        else:
            counter += int(m/f)
            m, f = f, m % f
    return str(counter)

# Should be 1
print(solution(2, 1))

# Should be 4
print(solution(4, 7))

print(solution(2, 4))