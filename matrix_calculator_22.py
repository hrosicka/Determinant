import tkinter as tk
import numpy as np
import customtkinter
from CTkMessagebox import CTkMessagebox
from determinant import Matrix


class MatrixCalculator22:
    """
    This class creates a GUI for calculating the determinant of a matrix.
    """

    def __init__(self, master):
        self.master = master  # Reference to the main window

        # Create the matrix calculator window as a Toplevel
        self.calculator_window = tk.Toplevel(master)
        self.calculator_window.title("2x2 Matrix Determinant Calculator")
        self.calculator_window.config(bg="#293241")

        # Frame for matrix input
        self.matrix_frame = tk.Frame(self.calculator_window, bg="#293241")
        self.matrix_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Labels and entry fields for matrix elements
        self.matrix_elements = {}
        for row in range(2):
            for col in range(2):
                entry = customtkinter.CTkEntry(self.matrix_frame, justify=tk.RIGHT)
                entry.grid(row=row, column=col + 1, padx=3, pady=3)
                self.matrix_elements[f"{row},{col}"] = entry

        # Button to trigger calculation
        self.calculate_button = customtkinter.CTkButton(self.calculator_window,
                                                        text="Calculate Determinant",
                                                        command=self.calculate_determinant22,
                                                        corner_radius=5,
                                                        width=150,
                                                        text_color="#EEEEEE",
                                                        fg_color="#293241",
                                                        hover_color="#EE6C4D",
                                                        border_width=1,
                                                        border_color="#EE6C4D",
                                                        font=customtkinter.CTkFont(size=14,)) #weight="bold"

        self.calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=15)

        # Label to display determinant
        self.determinant_label = tk.Label(self.calculator_window, 
                                          text="Determinant: ",
                                          bg="#293241",
                                          fg="white")
        
        self.determinant_label.grid(row=4, column=0, columnspan=2, padx=5, pady=15)

    def calculate_determinant22(self):
        # Get matrix elements from entry fields and convert to list
        matrix_data = []
        for row in range(2):
            row_data = []
            for col in range(2):
                element_str = self.matrix_elements[f"{row},{col}"].get()
                try:
                    element = float(element_str)
                    row_data.append(element)
                except ValueError:
                    self.determinant_label.config(text="Invalid matrix data. Enter numbers only.")
                    CTkMessagebox(title="Error", 
                        message="Invalid matrix data. Enter numbers only.",
                        height=150,
                        width=300,
                        bg_color="#3E4754",
                        fg_color="#293241",
                        title_color="#EEEEEE",
                        text_color="#EEEEEE",
                        button_text_color="#EEEEEE",
                        button_width=80,
                        button_color="#293241",
                        cancel_button_color="#EEEEEE",
                        button_hover_color="#EE6C4D",
                        border_width=1,
                        border_color="#3E4754")
                    return

            matrix_data.append(row_data)

        # Convert matrix data to NumPy array
        matrix = np.array(matrix_data)

        # Create Matrix object and calculate determinant
        matrix_object = Matrix(matrix)
        determinant = matrix_object.determinant()

        # Update determinant label
        self.determinant_label.config(text=f"Determinant: {determinant}")