"""
GUI Calculator Application using Tkinter.
This module provides a graphical interface for the Calculator class.
"""
import tkinter as tk
from tkinter import messagebox
from calculator import Calculator


class CalculatorGUI:
    """GUI wrapper for the Calculator class."""

    def __init__(self, root):
        """Initialize the calculator GUI."""
        self.root = root
        self.root.title("TDD Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.calculator = Calculator()
        self.current_input = ""
        self.first_operand = None
        self.operation = None

        self._create_widgets()

    def _create_widgets(self):
        """Create and layout all GUI widgets."""
        # Display frame
        display_frame = tk.Frame(self.root, bg="lightgray", pady=10)
        display_frame.pack(fill=tk.BOTH, expand=False)

        # Display entry
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 24),
            justify="right",
            bd=10,
            bg="white"
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=5)

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button layout
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*', '^'],  # added '^' power button
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        # Create buttons
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                button = tk.Button(
                    buttons_frame,
                    text=btn_text,
                    font=("Arial", 18),
                    command=lambda x=btn_text: self._on_button_click(x)
                )
                button.grid(row=row_idx, column=col_idx, sticky="nsew", padx=2, pady=2)

        # Configure grid weights for responsive layout
        max_cols = max(len(r) for r in buttons)
        for i in range(len(buttons)):
            buttons_frame.rowconfigure(i, weight=1)
        for j in range(max_cols):
            buttons_frame.columnconfigure(j, weight=1)

    def _on_button_click(self, char):
        """Handle button click events."""
        if char.isdigit():
            self._handle_digit(char)
        elif char in ['+', '-', '*', '/', '^']:
            self._handle_operation(char)
        elif char == '=':
            self._handle_equals()
        elif char == 'C':
            self._handle_clear()

    def _handle_digit(self, digit):
        """Handle digit button press."""
        self.current_input += digit
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_input)

    def _handle_operation(self, op):
        """Handle operation button press."""
        if self.current_input:
            self.first_operand = float(self.current_input)
            self.operation = op
            self.current_input = ""
            self.display.delete(0, tk.END)

    def _handle_equals(self):
        """Handle equals button press."""
        if self.first_operand is not None and self.operation and self.current_input:
            try:
                second_operand = float(self.current_input)
                result = self._calculate(self.first_operand, second_operand, self.operation)

                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))

                # Reset state
                self.current_input = str(result)
                self.first_operand = None
                self.operation = None
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                self._handle_clear()

    def _calculate(self, a, b, operation):
        """Perform calculation using the Calculator class."""
        if operation == '+':
            return self.calculator.add(a, b)
        elif operation == '-':
            return self.calculator.subtract(a, b)
        elif operation == '*':
            return self.calculator.multiply(a, b)
        elif operation == '/':
            return self.calculator.divide(a, b)
        elif operation == '^':
            return self.calculator.power(a, b)

    def _handle_clear(self):
        """Handle clear button press."""
        self.current_input = ""
        self.first_operand = None
        self.operation = None
        self.display.delete(0, tk.END)


def main():
    """Main entry point for the calculator application."""
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
