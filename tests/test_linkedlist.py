import unittest
from retos.reto3_linkedlist import add_task, find_by_id, find_by_priority

class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        add_task(1, "Probar DLL", 2)
        tarea = find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea["id"], 1)
        self.assertEqual(tarea["descripcion"], "Probar DLL")
        self.assertEqual(tarea["prioridad"], 2)

    def test_find_non_existent(self):
        tarea = find_by_id(999)
        self.assertIsNone(tarea)

    def test_find_by_priority_multiple(self):
        add_task(2, "Hacer la tarea", 1)
        add_task(3, "Estudiar", 1)
        add_task(4, "Ir al baño", 2)
        resultado = find_by_priority(1)
        ids = [t["id"] for t in resultado]
        self.assertCountEqual(ids, [2, 3])

if __name__ == "__main__":
    unittest.main()
