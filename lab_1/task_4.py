from enum import StrEnum


class TaskStatus(StrEnum):
    COMPLETED = "completed"
    IN_PROGRESS = "in progress"
    WAITING = "waiting"


def add_task(task_name: str, tasks: dict[str, TaskStatus], status: TaskStatus=TaskStatus.WAITING) -> bool:
    if task_name in tasks or status not in TaskStatus:
        return False

    tasks[task_name] = status
    return True


def delete_task(task_name: str, tasks: dict[str, TaskStatus]) -> bool:
    if task_name not in tasks:
        return False

    del tasks[task_name]
    return True


def change_task_status(task_name: str, new_status: TaskStatus, tasks: dict[str, TaskStatus]) -> bool:
    if task_name not in tasks or new_status not in TaskStatus:
        return False

    tasks[task_name] = new_status
    return True


def get_tasks_by_status(filter_status: TaskStatus, tasks: dict[str, TaskStatus]) -> dict[str, TaskStatus]:
    return {task: status for task, status in tasks.items() if status == filter_status}



def print_tasks(title: str, tasks: dict[str, TaskStatus]) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    if not tasks:
        print("No tasks to show.")
        return
    for task, status in tasks.items():
        print(f"Task: {task:<30} | Status: {status}")
    print()


def main() -> None:
    tasks = {
        "Prepare report": TaskStatus.IN_PROGRESS,
        "Update database": TaskStatus.COMPLETED,
        "Meet with client": TaskStatus.WAITING,
        "Write technical documentation": TaskStatus.WAITING,
        "Optimize algorithm": TaskStatus.COMPLETED,
        "Fix bugs in code": TaskStatus.WAITING,
        "Conduct code review": TaskStatus.WAITING,
    }

    print_tasks("Initial Tasks", tasks)

    print("Adding new task 'Design UI' with status 'in progress':")
    if add_task("Design UI", tasks, TaskStatus.IN_PROGRESS):
        print("=> Task added successfully.")
    else:
        print("=> Failed to add task.")

    print("Deleting task 'Update database':")
    if delete_task("Update database", tasks):
        print("=> Task deleted successfully.")
    else:
        print("=> Failed to delete task.")

    print("Changing status of 'Fix bugs in code' to 'in progress':")
    if change_task_status("Fix bugs in code", TaskStatus.IN_PROGRESS, tasks):
        print("=> Task status changed successfully.")
    else:
        print("=> Failed to change task status.")

    print_tasks("Final Tasks", tasks)

    waiting_tasks = get_tasks_by_status(TaskStatus.WAITING, tasks)
    print_tasks("Tasks with Status 'waiting'", waiting_tasks)


if __name__ == "__main__":
    main()
