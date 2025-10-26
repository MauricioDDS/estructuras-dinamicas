"""
Stack (Pila) implementado con lista enlazada simple.

TODO:
- Implementa Node (valor, next)
- Implementa Stack con operaciones: push, pop, peek, is_empty, size
- Garantiza que push y pop sean O(1)

Sugerencia:
- Mantén referencia a la "cabeza" (top) y un contador de tamaño.
"""

class Node:
    # TODO: implementar nodo simple
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, value):
        """Inserta en el tope. O(1)"""
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self):
        """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
        if self.head:
            top = self.head
            self.head = self.head.next
            self._size -= 1
            return top.value
        else:
            raise IndexError

    def peek(self):
        """Retorna el tope sin extraer. O(1). IndexError si vacía."""
        if self.head:
            top = self.head
            return top.value
        else:
            raise IndexError

    def is_empty(self):
        """True si no hay elementos. O(1)"""
        if self._size == 0:
            return True
        else:
            return False
        

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self._size
