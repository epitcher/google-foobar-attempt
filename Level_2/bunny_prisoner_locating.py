def solution(x, y):

    value = (x * (x + 1)) / 2
    increment = x

    for i in range(1, y):
        value += increment
        increment += 1

    return str(int(value))



print(solution(2, 3))
print(solution(5, 10))
print(solution(40000, 20000))