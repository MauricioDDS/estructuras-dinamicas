"""
Queue (Cola) implementada con lista doblemente enlazada.

TODO:
- Implementa DoubleNode (value, prev, next)
- Implementa Queue con operaciones: enqueue, dequeue, peek, is_empty, size
- Enqueue al final (tail) y dequeue al inicio (head) para O(1)

Sugerencia:
- Mantén punteros a head y tail, más un contador.
"""

class DoubleNode:
    # TODO: implementar nodo doble
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self._size = 0
        self.front = None
        self.rear = None
        
    # TODO: implementar cola enlazada doble
    def enqueue(self, value):
        """Inserta al final. O(1)"""
        new_node = DoubleNode(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node
        self._size += 1
            
    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        if self._size == 0:
            raise IndexError("Cola Vacia")
        temp = self.front.value
        self.front = self.front.next
        if self.front is not None:
            self.front.prev = None
        else:
            self.rear = None
        self._size -= 1
        return temp
        
    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        if self._size == 0:
            raise IndexError("Cola Vacia")
        return self.front.value

    def is_empty(self):
        """True si la cola está vacía. O(1)"""
        return self._size == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self._size
