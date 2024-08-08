time_work = 0
task_sum = 0
go_to_store = False


print("Начало рабочего дня")

while time_work != 8:
    time_work += 1
    print(time_work, "час")
    tasks = int(input("Сколько задач сделал Максим? "))
    task_sum += tasks
    call = int(input("Звонит жена. Взять трубку? (1 - да, 0 - нет) "))
    if call == 1:
        go_to_store = True
print("Рабочий день закончился. Количество решеных задач Максимом: ", task_sum)
if go_to_store == True:
    print("Зайти в магазин после работы")
    