import unittest
from retos.reto1_stack import validate_expression

class TestChallenge1Stack(unittest.TestCase):
    def test_simple_balanced_expression(self):
        # Arrange
        expresion = "({[]})"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertTrue(resultado)

    def test_simple_unbalanced_expression(self):
        # Arrange
        expresion = "({[]}))"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertFalse(resultado)

    def test_simple_incorrect_order_expression(self):
        # Arrange
        expresion = "{[}]"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertFalse(resultado)

    def test_empty_expression(self):
        # Arrange
        expresion = ""
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertTrue(resultado)

    def test_only_opening_characters(self):
        # Arrange
        expresion = "([{"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()
