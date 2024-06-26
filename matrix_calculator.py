import tkinter as tk
import numpy as np
import customtkinter
from message_box import *
from determinant import Matrix
from custom_button import *
from PIL import Image, ImageTk


class MatrixCalculator:
    """
    This class creates a GUI for calculating the determinant of a matrix.
    """

    def __init__(self, master, size_desc, dim):
        self.master = master  # Reference to the main window

        # Create the matrix calculator window as a Toplevel
        self.calculator_window = tk.Toplevel(master)
        self.calculator_window.title(size_desc)
        self.calculator_window.config(bg="#293241")

        ico = Image.open(os.path.join(dirname, 'icon.jpg'))
        photo = ImageTk.PhotoImage(ico)
        self.calculator_window.wm_iconphoto(False, photo)

        # Frame for matrix input
        self.matrix_frame = tk.Frame(self.calculator_window, bg="#293241")
        self.matrix_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Entry fields for matrix elements
        self.matrix_elements = {}
        for row in range(dim):
            for col in range(dim):
                entry = customtkinter.CTkEntry(self.matrix_frame,
                                               width=100,
                                               text_color="#EEEEEE",
                                               fg_color="#293241",
                                               border_width=1,
                                               justify=tk.RIGHT)
                entry.grid(row=row, column=col, padx=3, pady=3)
                entry.bind("<FocusOut>", lambda event, entry=entry: self.validate_entry(entry))
                self.matrix_elements[f"{row},{col}"] = entry


        # Button to fill empty cells with zero
        self.fill_zero_button = create_calculation_button(self.calculator_window,
                                                     text="Fill Empty Cells\n With Zero",
                                                     command=lambda: self.fill_with_zeros(dim))
        self.fill_zero_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)


        # Button to trigger calculation
        self.calculate_button = create_calculation_button(self.calculator_window,
                                                          text="Calculate\nDeterminant",
                                                          command=lambda: self.calculate_determinant(dim))
        self.calculate_button.grid(row=3, column=1, columnspan=1, padx=5, pady=15)

        # Label to display determinant
        self.determinant_label = tk.Label(self.calculator_window, 
                                          text="Determinant\n",
                                          bg="#293241",
                                          fg="white")
        self.determinant_label.grid(row=4, column=0, columnspan=2, padx=5, pady=15)

    def validate_entry(self, entry):
        element_str = entry.get()
        try:
            float(element_str)
            # Valid number, reset background color
            entry.configure(fg_color="#293241")
        except ValueError:
            # Invalid number, highlight the entry
            entry.configure(fg_color="#EE6C4D")

    def fill_with_zeros(self, dim):
        for row in range(dim):
            for col in range(dim):
                element_str = self.matrix_elements[f"{row},{col}"].get()
                if not element_str:
                    self.matrix_elements[f"{row},{col}"].insert(0, "0")
                    self.matrix_elements[f"{row},{col}"].configure(fg_color="#293241")

    def calculate_determinant(self, dim):
        # Get matrix elements from entry fields and convert to list
        matrix_data = []
        for row in range(dim):
            row_data = []
            for col in range(dim):
                element_str = self.matrix_elements[f"{row},{col}"].get()
                try:
                    element = float(element_str)
                    row_data.append(element)
                except ValueError:
                    output_text = f"Invalid number at row {row+1}, column {col+1}.\nEnter a number only."
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
        self.determinant_label.config(text=f"Determinant\n{determinant}")