import random
number = random.randint(1,30)
count = 0
while True:
    num_user = int(input("Введите число: "))
    count += 1
    if num_user > number:
        print("Ваше число больше загаданного. Пробуй еще")
    elif num_user < number:
        print("Ваше число меньше загаданного. Пробуй еще")
    else :
        print("Вы угадали загаданное число. Поздравляем! Число попыток", count)
        break