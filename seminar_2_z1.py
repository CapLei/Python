comment = int(input("Введите вашу оценку приложению "))

pozitive = 0
negative = 0

while comment != 0:
    if comment > 0:
        pozitive += 1
    else :
        negative += 1
    comment = int(input("Введите вашу оценку приложению "))

print(pozitive)
print(negative)