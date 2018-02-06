CREATE TABLE IF NOT EXISTS daily_planner (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_name TEXT NOT NULL,
  task_itself TEXT NOT NULL,
  due_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
