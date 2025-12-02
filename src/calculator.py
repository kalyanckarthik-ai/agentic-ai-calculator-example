"""
Calculator logic module.
This module contains the core calculation logic, separated from the GUI.
"""


class Calculator:
    """Simple calculator class for basic arithmetic operations."""

    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b

    def power(self, a, b):
        """Raise a to the power of b and return the result."""
        return a ** b

    def divide(self, a, b):
        """Divide a by b and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
