from typing import List
from datetime import datetime
from models import Task
from database import tasks_db, task_id_counter

def get_tasks() -> List[Task]:
    return tasks_db

def get_task(task_id: int) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None

def create_task(title: str, description: str) -> Task:
    global task_id_counter
    task_id_counter += 1
    new_task = Task(id=task_id_counter,
                    title=title,
                    description=description,
                    status="todo",
                    created_at=datetime.now())
    tasks_db.append(new_task)
    return new_task

def update_task(task_id: int, title: str, description: str, status: str) -> Task:
    for task in tasks_db:
        if task.id == task_id:
            task.title = title
            task.description = description
            task.status = status
            return task
    return None

def delete_task(task_id: int) -> bool:
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[index]
            return True
    return False

