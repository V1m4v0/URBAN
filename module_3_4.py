def get_multiplied_digits(number):  # Создаем функцию с параметром
    str_number = str(number)    # Присваиваем переменной число в строковом представлении
    first = int(str_number[0])  # Присваиваем переменной первую цифру. При преобразовании строки(str) в число(int)
    # первые нули убираются. int('00123') -> 123.
    if first == 0:  # Если цифра равна нулю
        first = number  # Присваиваем ей текущее значение параметра функции
    elif len(str_number) == 1: # Если количество символов равно одному
        return first # Возвращаем значение переменной
    else:
        return first * get_multiplied_digits(int(str_number[1:]))   # Возвращаем значение переменной умноженное на
        # результат работы этой же функции с числом



result = get_multiplied_digits(901332)
print(result)