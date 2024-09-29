alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def cesar_cipher(string, user_shift):
    char_list = [(alphavit[(alphavit.index(sym) + user_shift) % len(alphavit)]
                        if sym in alphavit else sym)
                        for sym in string]
    
    new_str = ''.join(char_list)
    return new_str

input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output_str = cesar_cipher(input_str, shift)

print('Зашифрованное сообщение: ', output_str)