videoCardsNumber = (int(input("Введите кол-во видеокарт: ")))

videoCards = []
newVideoCardsList = []
maxItem = 0

for item in range(videoCardsNumber):
    videoCards.append(int(input(f"Видеокарта {item + 1}: ")))
    
    
if videoCards[item] > maxItem:
    maxItem = videoCards[item]
    

for item in range(videoCardsNumber):
    if videoCards[item] != maxItem:
        newVideoCardsList.append(videoCards[item])
        
print()
print('Старый список видеокарт: [', end=' ')
for item in range(videoCardsNumber):
    print(videoCards[item], end=" ")
print(']')

print('Новый список видеокарт: [', end=' ')
for item in range(len(newVideoCardsList)):
    print(newVideoCardsList[item], end=" ")
print(']')


