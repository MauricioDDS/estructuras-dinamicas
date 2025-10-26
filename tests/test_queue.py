import unittest
from retos.reto2_queue import QueueManager

class TestChallenge2Queue(unittest.TestCase):
    def test_serve_in_fifo_order(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Ana")
        self.assertEqual(tiempo, 5)

    def test_state(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)
        gestor.add_person("Mauro", 4)
        self.assertEqual(gestor.state(), ["Ana", "Luis", "Mauro"])
        
    def test_serve_mixed(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)
        gestor.serve_person()
        gestor.add_person("Mauro", 4)
        self.assertEqual(gestor.state(), ["Luis", "Mauro"])

if __name__ == "__main__":
    unittest.main()
