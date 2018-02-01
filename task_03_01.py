"""
Напишите функцию get_days_to_new_year, которая возвращает количество
дней, оставшихся до нового года. Датой наступления нового года
считается 1 января. Функция должна корректно работать при запуске
в любом году, т. е. грядущий год должен вычисляться программно.
Для решения задачи понадобится стандартный модуль datetime
(или аналогичный из стандартной библиотеки) Требуется реализовать
только функцию, решение не должно осуществлять операций ввода-вывода.
"""
from datetime import date


def get_days_to_new_year():
    today = date.today()
    ny = date(today.year, 12, 31)
    return ny - today
