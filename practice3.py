a = int(input('Enter the number '))


def kat(n):
    s = 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            s += i
    return s == n

print(kat(a))
