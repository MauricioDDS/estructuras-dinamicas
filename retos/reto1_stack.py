"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

PARES = {')': '(', '}': '{', ']': '['}

def validate_expression(expression: str) -> bool:
    stack = Stack()
    for current in expression:
        if current in "([{":
            stack.push(current)
        elif current in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if PARES[current] != top:
                return False
    return stack.is_empty()