films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

my_film = []
movie = ''

movies_count = int(input('Сколько фильмов вы хотите добавить в список: '))

for _ in range(movies_count):
    movie = input("Введите название кинокартины: ")

    if movie in films:
        my_film.append(movie)
    else:
        print("Такого фильма нет в списке")

print(f'\nВаш список любимых фильмов: {my_film}')