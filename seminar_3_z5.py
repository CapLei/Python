orders_count = int(input("Введите кол-во заказов: "))

database = dict()

for i_order in range(orders_count):
    customer, pizza_name, count = input('{} заказ: ' .format(i_order + 1)).split()
    count = int(count)
    
    if customer not in database:
        database[customer] = {pizza_name: count}
    else:
        if pizza_name in database[customer]:
            database[customer][pizza_name] += count
        else:
            database[customer][pizza_name] = count
            
for customer in sorted(database.keys()):
    print('{}:'.format(customer))
    for pizza_name in sorted(database[customer].keys()):
        print('         {}: {}'.format(pizza_name, database[customer][pizza_name]))
        