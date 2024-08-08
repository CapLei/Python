total_card = int(input("Введите общее число карточек "))
sum_card = 0

for i in range(1, total_card + 1):
    sum_card += i
    
for i in range(total_card - 1):
    card = int(input("Номер оставшихся карт "))
    sum_card -= card
print("Номер потерянной карты: ", sum_card)