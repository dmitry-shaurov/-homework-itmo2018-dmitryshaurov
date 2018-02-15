"""
Требуется реализовать генератор случайных паролей указанной длины.
В пароле можно использовать любые символы в верхнем и нижнем регистре.
Например: password_generator(16), вернет случайный пароль длиной 16 символов.
Пригодится стандартный модуль random
В решении не должно присутствовать операций ввода-вывода.

Имя файла:
task_generator_password.py
Имя функции:
password_generator
Возвращаемое значение:
Генератор
Кол-во баллов:
2
"""
import random
import string

def password_generator(n):
    while True:
        pwd = ''
        for i in range(n):
            pwd = pwd + random.choice(string.ascii_letters)
        yield pwd

# gen = password_generator(20)
# print(next(gen))
# print(next(gen))
# print(next(gen))
