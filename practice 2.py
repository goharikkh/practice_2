a = int(input('Enter the number '))


def baj(n):
    res = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            res.append(i)
    res.append(n)
    return res


print(baj(a))

