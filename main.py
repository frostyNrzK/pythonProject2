def enter_time():
    while True:
        time = int(input('Введите время (0-23):'))
        if time < 0 or time > 23:
            print('Некорректное время')
        else:
            return time

time = enter_time()
if 5 <= time <= 12:
    print('Сейчас Утро!')
if 13 <= time <= 16:
    print('Сейчас День')
if 17 <= time <= 20:
    print('Сейчас Вечер!')
if 21 <= time <= 23 or 0 <= time <= 4:
    print('Сейчас Ночь!')



