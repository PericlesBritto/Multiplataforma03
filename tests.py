import unittest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime
from models import Task

client = TestClient(app)

class TestTasksAPI(unittest.TestCase):

    def test_create_task(self):
        response = client.post("/tasks/", json={"title": "Nova Tarefa", "description": "Descrição da nova tarefa"})
        self.assertEqual(response.status_code, 201)
        task = response.json()
        self.assertEqual(task['title'], "Nova Tarefa")
        self.assertEqual(task['description'], "Descrição da nova tarefa")
        self.assertEqual(task['status'], "todo")
        self.assertTrue('created_at' in task)

    def test_read_task(self):
        response = client.post("/tasks/", json={"title": "Tarefa para leitura", "description": "Descrição da tarefa"})
        task = response.json()
        task_id = task['id']
        response = client.get(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], "Tarefa para leitura")

    def test_update_task(self):
        response = client.post("/tasks/", json={"title": "Tarefa para atualizar", "description": "Descrição da tarefa"})
        task = response.json()
        task_id = task['id']
        response = client.put(f"/tasks/{task_id}", json={"title": "Tarefa atualizada", "description": "Descrição atualizada", "status": "doing"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], "Tarefa atualizada")
        self.assertEqual(response.json()['status'], "doing")

    def test_delete_task(self):
        response = client.post("/tasks/", json={"title": "Tarefa para deletar", "description": "Descrição da tarefa"})
        task = response.json()
        task_id = task['id']
        response = client.delete(f"/tasks/{task_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], "Task deleted successfully")

if __name__ == '__main__':
    unittest.main()
