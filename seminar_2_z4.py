zp_year = 0
for i in range(1, 13):
    zp = int(input(f"Введите Вашу заработную плату за {i} месяц: "))
    zp_year += zp
print("Средняя зарплата за год ", zp_year / 12)