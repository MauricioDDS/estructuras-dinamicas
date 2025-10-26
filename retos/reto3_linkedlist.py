"""
Reto 3: Gestor de tareas con DoublyLinkedList.

Funciones a implementar (usa DoublyLinkedList de estructuras/linkedlist.py):
    - add_task(id:int, descripcion:str, prioridad:int) -> None
    - find_by_id(id:int) -> dict|None
    - find_by_priority(prioridad:int) -> list[dict]

Nota:
- La lista interna debe almacenar dicts con llaves: id, descripcion, prioridad.
"""

from estructuras.linkedlist import DoublyLinkedList

_lista_tareas = DoublyLinkedList()

class Task:
    def __init__(self, task_id, descripcion, prioridad):
        self.id = task_id
        self.description = descripcion
        self.priority = prioridad

def add_task(task_id: int, descripcion: str, prioridad: int) -> None:
    nueva_tarea = Task(task_id, descripcion, prioridad)
    _lista_tareas.append(nueva_tarea)

def find_by_id(task_id: int):
    tarea = _lista_tareas.find_by_id(task_id)
    if tarea is None:
        return None
    return {
        "id": tarea.id,
        "descripcion": tarea.description,
        "prioridad": tarea.priority
    }

def find_by_priority(prioridad: int):
    tareas = _lista_tareas.find_by_prioridad(prioridad)
    resultado = []
    for tarea in tareas:
        resultado.append({
            "id": tarea.id,
            "descripcion": tarea.description,
            "prioridad": tarea.priority
        })
    return resultado