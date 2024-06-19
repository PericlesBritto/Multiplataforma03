from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from datetime import datetime
import services

app = FastAPI(
    title="API de Gerenciamento de Tarefas",
    description="Esta é uma API simples para gerenciar tarefas com operações básicas de CRUD.",
    version="1.0.0",
)

# Modelos Pydantic
class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Tarefa exemplo",
                "description": "Descrição da tarefa exemplo",
                "status": "todo",
                "created_at": "2023-06-18T15:30:00"
            }
        }

# Endpoints
@app.get("/tasks/", response_model=List[Task], tags=["Tarefas"])
def read_tasks():
    """
    Retorna todas as tarefas cadastradas.
    """
    return services.list_tasks()

@app.get("/tasks/{task_id}", response_model=Task, tags=["Tarefas"])
def read_task(task_id: int):
    """
    Retorna uma tarefa específica pelo seu ID.
    """
    task = services.get_single_task(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.post("/tasks/", response_model=Task, status_code=201, tags=["Tarefas"])
def create_task(title: str, description: str):
    """
    Cria uma nova tarefa.
    """
    return services.add_task(title, description)

@app.put("/tasks/{task_id}", response_model=Task, tags=["Tarefas"])
def update_task(task_id: int, title: str, description: str, status: str):
    """
    Atualiza uma tarefa existente.
    """
    task = services.modify_task(task_id, title, description, status)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task

@app.delete("/tasks/{task_id}", tags=["Tarefas"])
def delete_task(task_id: int):
    """
    Deleta uma tarefa existente.
    """
    if not services.remove_task(task_id):
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"message": "Tarefa deletada com sucesso"}
