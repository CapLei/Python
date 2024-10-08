from csv import DictReader, DictWriter
from os.path import exists
import shutil

class NameErrore(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:
            
            first_name = input('Имя: ')
            if len(first_name) < 2:
                raise NameError("Слишком короткое имя")
            secound_name = input('Введите фамилию: ')
            if len(secound_name) < 4:
                raise NameError("Слишком короткая фамилия")
            phone_number = input('Введите номер телефона: ')
            if len(secound_name) < 11:
                raise NameError("Слишком короткий номер")
        except NameError as err:
            print(err)
        else:
            flag = True

    return [first_name, secound_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'secound_name', 'phone_number'])
        f_w.writeheader()
        
        
def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    new_obj = {'first_name': user_data[0], 'secound_name': user_data[1], 'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)

def read_file(file_name):
     with open(file_name, encoding='utf-8') as data:
         f_r = DictReader(data)
         return list(f_r) #список со словарями


def remouve_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    if search <= len(res):
        
        res.pop(search - 1)
        standart_write(file_name, res)
    else:
        print('Введен неверный номер строки ')
        
        
def standart_write(first_name, res):
        with open(file_name, 'w', encoding='utf-8', newline='') as data:
            f_w = DictWriter(data, fieldnames=['first_name', 'secound_name', 'phone_number'])
            f_w.writeheader()
            f_w.writerows(res)


def copy_data(file_name):
    shutil.copy('/Users/fuvis/Desktop/Seminar/phone.csv', '/Users/fuvis/Desktop/Seminar/phone2.csv')
    
         
         
         

file_name = 'phone.csv'     
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутвует, пожалуйста создайте файл ')
                continue
            print(*read_file(file_name))
        elif command == 'd':
            if not exists(file_name):
                print('Файл отсутвует, пожалуйста создайте файл ')
                continue
            remouve_row(file_name)
        elif command == 'c':
            if not exists(file_name):
                print('Файл отсутсвует, пожалуйста создайте файл ')
                continue
            copy_data(file_name)
            
main()

"""
реализовать копирование данных из файла А в файл B.
написать отдельную функцию copy_data:
прочитать список словарей (read_file)
и записать его в новый файл используя функцию standart_write
дополнить функцию main
из phone.csv в phone2.csv
"""