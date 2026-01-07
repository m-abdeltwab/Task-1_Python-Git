# 5.Task Scheduler (Logic Version)
# ==============================
# User adds tasks with:
# name
# priority (1–5)
# deadline (string)
# ==============================
# Program outputs tasks sorted by:
# 1.  priority
# 2.  earliest deadline
from datetime import date


class Task:
    def __init__(self, name: str, priority, deadline=None) -> None:
        # Verification

        # ------ name
        if not name or not name.strip():
            raise ValueError("Task Name Can't be Empty.")
        # ------ priority
        if not isinstance(priority, int):
            raise ValueError("Priority Should Be Integer .")
        if not (1 <= priority <= 5):
            raise ValueError("Priority Should from 1 to 5 .")
        # ------ deadline
        if deadline is not None:
            try:
                (
                    year,
                    month,
                    day,
                ) = map(int, deadline.split(","))
                self.deadline = date(year, month, day)
            except:
                raise ValueError("The deadline should be in (year, month, day) format.")

        else:
            self.deadline = deadline

        # Attributes
        self.name: str = name
        self.priority: int = priority

    # Dunder Methods
    def __lt__(self, other):
        return (-self.priority, self.deadline) < (-other.priority, other.deadline)

    def __str__(self):
        return f"Task: {self.name.ljust(7)}, priority: {self.priority}, deadline: {self.deadline}"


class TaskManager:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, name, priority, deadline):
        self.tasks.append(Task(name, priority, deadline))

    def print_tasks(self):
        for task in sorted(self.tasks):
            print("--------------------------------------------------")
            print(task)
            print("--------------------------------------------------")


tm = TaskManager()
tm.add_task("Gym", 2, "2026, 1, 10")
tm.add_task("clean", 1, "2026, 1, 5")
tm.add_task("reading", 1, "2026, 3, 7")
tm.add_task("reading", 1, "2026, 2, 1")
tm.print_tasks()
