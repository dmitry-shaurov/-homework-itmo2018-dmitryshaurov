"""
Реализуйте модуль number_system для перевода числа из одной системы
счисления в другую. Модуль должен содержать 6 функций для перевода
из десятичной системы счисления в двоичную, восьмеричную,
шестнадцатиричную и наоборот.
(!) Запрещено использовать встроенные функции/методы, решающие
эту задачу. Подсказка. Не спешите писать 6 разных реализаций,
подумайте, можно ли написать универсальный алгоритм перевода.
В решении не должно присутствовать операций ввода-вывода. Ситуации,
когда в исходном числе есть не допустимые цифры (буквы), игнорируются.
Материал по переводу из одной СС в другую

#dec2bin(number) # возвращает str
#dec2oct(number) # возвращает str
#dec2hex(number) # возвращает str
#bin2dec(number) # возвращает int
#oct2dec(number) # возвращает int
#hex2dec(number) # возвращает int

"""

def dec2bin(number):
    result = []
    while number // 2 >= 2:
        result.append(str(number%2))
        number = number // 2
    result.append(str(number%2))
    result.append(str(number//2))
    result_list = result[::-1]
    result_string = ''.join(result_list)
    return result_string

def dec2oct(number):
    result = []
    while number // 8 >= 8:
        result.append(str(number%8))
        number = number // 8
    result.append(str(number%8))
    result.append(str(number//8))
    result_list = result[::-1]
    result_string = ''.join(result_list)
    return result_string


def dec2hex(number):
    result = []
    while number // 16 >= 16:
        if number % 16 == 10:
            result.append("a")
            number = number // 16
        elif number % 16 == 11:
            result.append("b")
            number = number // 16
        elif number % 16 == 12:
            result.append("c")
            number = number // 16
        elif number % 16 == 13:
            result.append("d")
            number = number // 16
        elif number % 16 == 14:
            result.append("e")
            number = number // 16
        elif number % 16 == 15:
            result.append("f")
            number = number // 16
        else:
            result.append(str(number%16))
            number = number // 16
    if number % 16 == 10:
        result.append("a")
    elif number % 16 == 11:
            result.append("b")
    elif number % 16 == 12:
        result.append("c")
    elif number % 16 == 13:
        result.append("d")
    elif number % 16 == 14:
        result.append("e")
    elif number % 16 == 15:
        result.append("f")
    else:
        result.append(str(number %16))
    if number // 16 == 10:
        result.append("a")
    elif number // 16 == 11:
            result.append("b")
    elif number // 16 == 12:
        result.append("c")
    elif number // 16 == 13:
        result.append("d")
    elif number // 16 == 14:
        result.append("e")
    elif number // 16 == 15:
        result.append("f")
    else:
        result.append(str(number // 16))
    result_list = result[::-1]
    result_string = ''.join(result_list)
    return result_string


def bin2dec(number):
    a = len(number) - 1
    result = 0
    for i in number:
        result += int(i)*(2**a)
        a -= 1
    return result

def oct2dec(number):
    a = len(number) - 1
    result = 0
    for i in number:
        result += int(i)*(8**a)
        a -= 1
    return result


def hex2dec(number):
    a = len(number) - 1
    result = 0
    for i in number:
        if i == "A" or i == "a":
            i = 10
            result += int(i)*(16**a)
            a -= 1
        elif i == "B" or i == "b":
            i = 11
            result += int(i)*(16**a)
            a -= 1
        elif i == "C" or i == "c":
            i = 12
            result += int(i)*(16**a)
            a -= 1
        elif i == "D" or i == "d":
            i = 13
            result += int(i)*(16**a)
            a -= 1
        elif i == "E" or i == "e":
            i = 14
            result += int(i)*(16**a)
            a -= 1
        elif i == "F" or i == "f":
            i = 15
            result += int(i)*(16**a)
            a -= 1
        else:
            result += int(i)*(16**a)
            a -= 1
    return result
