from typing import List
from models import Task
from repositories import get_tasks, get_task, create_task, update_task, delete_task

def list_tasks() -> List[Task]:
    return get_tasks()

def get_single_task(task_id: int) -> Task:
    return get_task(task_id)

def add_task(title: str, description: str) -> Task:
    return create_task(title, description)

def modify_task(task_id: int, title: str, description: str, status: str) -> Task:
    return update_task(task_id, title, description, status)

def remove_task(task_id: int) -> bool:
    return delete_task(task_id)
