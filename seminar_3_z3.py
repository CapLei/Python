list = [1, 4, -3, 0, 10]
print("Изначальный список: ", list)

for i in range(len(list) - 1):
    for j in range(len(list) -1 - i):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print('Отсортированный список: ', list)