def solution(arr, n):
    result = []
    for i in range(len(arr)):
        if len(arr) % 2 == 1 and i % 2 == 0:
            result.append(arr[i] + n)
        elif len(arr) % 2 == 0 and i % 2 == 1:
            result.append(arr[i] + n)
        else:
            result.append(arr[i])
    return result

arr1 = [49, 12, 100, 276, 33]
n1 = 27
print(solution(arr1, n1))

arr2 = [444, 555, 666, 777]
n2 = 100
print(solution(arr2, n2))