def monoton(data):
    for i in range(0, len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True


n = int(input('Enter the number: '))
res = []
while n != 0:
    res.append(n)
    n = int(input('Enter the number: '))
print(res)

print(monoton(res))
