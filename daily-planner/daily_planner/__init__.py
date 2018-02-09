import sys

from daily_planner import storage

get_connection = lambda: storage.connect('daily_planner.sqlite')

def main():
    with get_connection() as conn:
        storage.initialize(conn)
    actions = {
        "1" : action_show_tasks_in_table,
        "2" : action_add_task,
        "3" : action_edit_task,
        "4" : action_finish_task,
        "5" : action_start_task_again,
        "6" : action_show_all_entries,
        "7" : action_show_tasks,
        "q" : action_exit,
    }

    action_show_tasks()

    while 1: # while True
        cmd = input("\nВведите команду:")
        action = actions.get(cmd)

        if action:
            try:
                action()
            except Exception as e:
                print(e)
        else:
            print("Unknown command")

def action_show_tasks():
    """shows tasks"""
    print("""
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Вывести все записи БД
7. Повторить вывод меню
q. Выход
""")

def action_show_tasks_in_table():
    """show all the tasks in the table"""
    due_date = input("За какой день Вы хотите увидеть задачи? (default is today)")
    with get_connection() as conn:
        storage.show_tasks_in_table(conn, due_date)


def action_add_task():
    """adds a task"""
    task = input("\nВведите задачу:")
    due_date = input("\nВведитие планируемую дату выполнения: (default is today) ")
    activities = input("\nЧто имеено Вы планируете делать? ")
    with get_connection() as conn:
        storage.add_task(conn, task, activities, due_date)
    print("The task has beed added")

def action_edit_task():
    """edit a task"""
    pk = int(input("\nВведите задачу, которую Вы хотите отредактировать: "))
    with get_connection() as conn:
        storage.edit_task(conn, pk)

def action_finish_task():
    """finishes a task"""
    pk = int(input("\nВведите задачу, которую Вы хотите завершить:"))
    with get_connection() as conn:
        storage.finish_task(conn, pk)

def action_start_task_again():
    """starts a task again"""
    pk = int(input("\nВведите задачу, которую Вы хотите начать заново:"))
    with get_connection() as conn:
        storage.start_task_again(conn, pk)

def action_exit():
    """Выход"""
    sys.exit(0)


def action_show_all_entries():
    """shows all the table"""
    with get_connection() as conn:
        storage.show_all_entries(conn)
