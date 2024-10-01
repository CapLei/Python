def count_unique_characters(string):
    lower_string = string.lower()
    unique_characters = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    print(unique_characters)
    
    return len(unique_characters)

message = "Сегодня сложный день, скорее бы пройти проверку и выдохнуть"
unique_count = count_unique_characters(message)

print("Количество уникальных символов в строке: ", unique_count)