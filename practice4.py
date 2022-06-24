def zip_(data1, data2):
    list = []
    for i in range(0, len(data1)):
        res = []
        res.append(data1[i])
        res.append(data2[i])
        list.append(res)
    return list


print(zip_([1, 2, 3], [2, 3, 4]))
