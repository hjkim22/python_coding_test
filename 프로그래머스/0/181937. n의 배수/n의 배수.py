def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0
print(solution(98, 2))
print(solution(34, 3))