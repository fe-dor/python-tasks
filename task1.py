# a = [2, 2, 2, 3, 5, 8, 23, 22, 34, 55, 89]
# b = [2, 2, 3, 4, 5, 6, 7, 8, 9, 20, 22, 22, 23]

b = [1, 2, 3]
a = [3, 3, 3]


def func():
    result = []
    for i in set(a):
        for j in b:
            if i == j:
                result.append(i)
                break
    return result


def func2(list1, list2):
    result = []
    for elem in set(list1):
        if elem in list2:
            result.append(elem)
    return result


print(func())
print(func2(a, b))
