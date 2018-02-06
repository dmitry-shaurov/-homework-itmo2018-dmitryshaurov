def show_tasks():
    return "1. Вывести список задач\n"

def add_task():
    return "2. Добавить задачу\n"

def edit_task():
    return "3. Отредактировать задачу\n"

def finish_task():
     return "4. Завершить задачу\n"

def start_again_task():
    return "5. Начать задачу сначала\n"

def exit_from_planner():
     return "6. Выход\n"

a = show_tasks()
b = add_task()
c = edit_task()
d = finish_task()
e = start_again_task()
f = exit_from_planner()
daily_planner = {   1: a,
                    2 : b,
                    3 : c,
                    4 : d,
                    5 : e,
                    6 : f
                }
i = 1
while  i in range(1,7):
    with open("text.txt") as f:
        print(f.read())
        i = int(input("Введите число: \n"))
        print(daily_planner.get(i))
