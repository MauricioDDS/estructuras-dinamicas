"""
Lista doblemente enlazada (DLL) para gestionar tareas.

TODO:
- Implementa DoubleNode (id, descripcion, prioridad, prev, next)
- Implementa DoublyLinkedList con: append, prepend, remove_by_id, find_by_id, find_by_prioridad, iter_forward, iter_backward, size
- Mantén head, tail y contador para O(1) en inserciones a extremos.

Nota:
- 'find' será O(n) lineal.
"""

class DoubleNode:
     def __init__(self, task):
        self.id = task.id
        self.description = task.description
        self.priority = task.priority
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    def append(self, task):
        """Inserta al final. O(1)"""
        new_node = DoubleNode(task)
        if self._size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1
        
    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        new_node = DoubleNode(task)
        if self._size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        current = self.head
        while current:
            if current.id == task_id:
                if self._size == 1:
                    self.head = self.tail = None
                elif current == self.head:
                    self.head = current.next
                    self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                current.next = current.prev = None
                self._size -= 1
                return True
            current = current.next
        return False
        
    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        if self._size == 0:
            raise IndexError("Lista Vacia")
        current = self.head
        while current:
            if current.id == task_id:
                return current
            current = current.next
        return None

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        if self._size == 0:
            raise IndexError("Lista Vacia")
        results = []
        current = self.head
        while current is not None:
            if current.priority == prioridad:
                results += [current]
            current = current.next
        return results

    def iter_forward(self):
        """Generador hacia adelante."""
        if self._size == 0:
            raise IndexError("Lista Vacia")
        items = []
        current = self.head
        while current is not None:
            items += [current]
            current = current.next
        return items

    def iter_backward(self):
        """Generador hacia atrás."""
        if self._size == 0:
            raise IndexError("Lista Vacia")
        items = []
        current = self.tail
        while current is not None:
            items += [current]
            current = current.prev
        return items

    def size(self):
        """Cantidad de nodos. O(1)"""
        return self._size
