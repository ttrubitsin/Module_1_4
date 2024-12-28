def get_multiplied_digits(number):
    if isinstance(number, int) and number < 0: # проверка на отрицательное число
        return get_multiplied_digits(-number) # вызов функции с отрицательным значением для обработки числа с "-"
    str_number = str(number) # преобразование числа в строку
    if len(str_number) > 1: # проверка на длину строки
        first = int(str_number[0]) # условие выполняется - извлекаем первую цифру как целое число
        rest = int(str_number[1:]) # - извлекаем оставшиеся цифры
        return first * get_multiplied_digits(rest) # возвращаем произведение первой цифры на результат
    else:                                          # рекурсивного вызова функции оставшмися цифрами "rest"
        return int(str_number)            # в случае если длина строки равна 1 - возвращаем целое число
result = get_multiplied_digits(5022)
print(result)
