text = input('Введите текст: ')
vowels = [i for i in text if i in 'ауоыиэяюёе']
print('Список гласных букв: ', vowels)
print('Длина списка: ', len(vowels))