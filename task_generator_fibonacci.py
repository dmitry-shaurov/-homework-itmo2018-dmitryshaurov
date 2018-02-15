"""
Реализовать генератор чисел Фибоначчи.
Генератор принимает один обязательный аргумент - количество элементов последовательности.
В решении не должно присутствовать операций ввода-вывода.

Имя файла:
task_generator_fibonacci.py
Имя функции:
fibonacci
Возвращаемое значение:
Генератор
"""

def fibonacci(n):
    a = 1
    b = 1
    yield 1
    yield 1
    for i in range(2, n):
            f = a + b
            a = b
            b = f
            yield f

# print(type(fibonacci(3)))
# for j in fibonacci(3):
#     print(j, end='  ')
