import tkinter as tk
import numpy as np
from message_box import *
from determinant import Matrix
from custom_button import *


class MatrixCalculator55:
    """
    This class creates a GUI for calculating the determinant of a matrix.
    """

    def __init__(self, master):
        self.master = master  # Reference to the main window

        # Create the matrix calculator window as a Toplevel
        self.calculator_window = tk.Toplevel(master)
        self.calculator_window.title("5x5 Matrix")
        self.calculator_window.config(bg="#293241")

        # Frame for matrix input
        self.matrix_frame = tk.Frame(self.calculator_window, bg="#293241")
        self.matrix_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Labels and entry fields for matrix elements
        self.matrix_elements = {}
        for row in range(5):
            for col in range(5):
                entry = customtkinter.CTkEntry(self.matrix_frame, width=100, justify=tk.RIGHT)
                entry.grid(row=row, column=col + 1, padx=3, pady=3)
                self.matrix_elements[f"{row},{col}"] = entry

        # Button to trigger calculation
        self.calculate_button = create_calculation_button(self.calculator_window,
                                                          text="Calculate\nDeterminant",
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
                    output_text = f"Invalid number at row {row+1}, column {col+1}. Enter a number only."
                    self.determinant_label.config(text=output_text)
                    show_error_message(message=output_text)
                    return

            matrix_data.append(row_data)

        # Convert matrix data to NumPy array
        matrix = np.array(matrix_data)

        # Create Matrix object and calculate determinant
        matrix_object = Matrix(matrix)
        determinant = matrix_object.determinant()

        # Update determinant label
        self.determinant_label.config(text=f"Determinant: {determinant}")