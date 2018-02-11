import os.path as Path
import sqlite3
from datetime import date

SQL_SELECT_ALL_TASKS = """
    SELECT
        id, task, activities, due_date, status
    FROM
        daily_planner
    WHERE
        due_date=?
"""

SQL_INSERT_A_TASK = """
    INSERT INTO daily_planner (task, activities, due_date) VALUES (?, ?, ?)
"""

SQL_UPDATE_A_TASK = """
    UPDATE daily_planner SET activities=? WHERE id=?
"""

SQL_CHANGE_STATUS_FOR_A_TASK = """
    UPDATE daily_planner SET status=? WHERE id=?
"""


def connect(db_name=None):
    """Connecting to BD"""
    if db_name is None:
        db_name = ':memory'
    conn = sqlite3.connect(db_name)
    return conn

def initialize(conn, creation_script=None):
    """ Инициализация структура БД"""
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__), 'resourses', 'schema.sql')
    with conn, open(creation_script) as f:
        conn.executescript(f.read())

def show_tasks_in_table(conn, due_date):
    """shows tasks in the table"""
    if not due_date:
        due_date = date.today()
    with conn:
        cursor = conn.cursor()
        cursor = cursor.execute(SQL_SELECT_ALL_TASKS, (due_date,))
    return cursor

def add_task(conn, task, activities, due_date):
    """Adds a task to the database"""
    if not task:
        raise RuntimeError("task can't be empty")
    if not due_date:
        due_date = date.today()
    with conn:
        conn.execute(SQL_INSERT_A_TASK, (task, activities, due_date))

def show_all_entries(conn):
    """shows_all_entries"""
    with conn:
        cursor = conn.cursor()
        cursor = cursor.execute("SELECT * FROM daily_planner")
    return cursor


def edit_task(conn, pk, activities):
    """Edits activities for the current task"""
    with conn:
        cursor = conn.cursor()
        cursor = cursor.execute("SELECT COUNT(*) FROM daily_planner")
        if pk > cursor.fetchone()[0]:
            raise RuntimeError("There is no such task")
        else:
            cursor = cursor.execute(SQL_UPDATE_A_TASK, (activities, pk))


def finish_task(conn, pk):
    """finishes a task"""
    with conn:
        conn.execute(SQL_CHANGE_STATUS_FOR_A_TASK, (1, pk))

def start_task_again(conn, pk):
    """starts a task again"""
    with conn:
        conn.execute(SQL_CHANGE_STATUS_FOR_A_TASK, (0, pk))
