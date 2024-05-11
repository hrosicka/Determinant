import tkinter as tk
import numpy as np
from determinant import Matrix


class MatrixCalculator55:
    """
    This class creates a GUI for calculating the determinant of a matrix.
    """

    def __init__(self, master):
        self.master = master  # Reference to the main window

        # Create the matrix calculator window as a Toplevel
        self.calculator_window = tk.Toplevel(master)
        self.calculator_window.title("Matrix Determinant Calculator")

        # Frame for matrix input
        self.matrix_frame = tk.Frame(self.calculator_window)
        self.matrix_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Labels and entry fields for matrix elements
        self.matrix_elements = {}
        for row in range(5):
            for col in range(5):
                entry = tk.Entry(self.matrix_frame, justify=tk.RIGHT)
                entry.grid(row=row, column=col + 1, padx=2, pady=2)
                self.matrix_elements[f"{row},{col}"] = entry

        # Button to trigger calculation
        self.calculate_button = tk.Button(self.calculator_window,
                                          text="Calculate Determinant",
                                          command=self.calculate_determinant55)
        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        # Label to display determinant
        self.determinant_label = tk.Label(self.calculator_window, text="Determinant: ")
        self.determinant_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def calculate_determinant55(self):
        # Get matrix elements from entry fields and convert to list
        matrix_data = []
        for row in range(5):
            row_data = []
            for col in range(5):
                element_str = self.matrix_elements[f"{row},{col}"].get()
                try:
                    element = float(element_str)
                    row_data.append(element)
                except ValueError:
                    self.determinant_label.config(text="Invalid matrix data. Enter numbers only.")
                    return

            matrix_data.append(row_data)

        # Convert matrix data to NumPy array
        matrix = np.array(matrix_data)

        # Create Matrix object and calculate determinant
        matrix_object = Matrix(matrix)
        determinant = matrix_object.determinant()

        # Update determinant label
        self.determinant_label.config(text=f"Determinant: {determinant}")