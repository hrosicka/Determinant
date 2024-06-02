# Improves DPI awareness for high-resolution displays (enables sharper visuals)
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

from matrix_calculator import *

# Main window class for the determinant calculator application
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window title
        self.title("Determinant Calculator")
        
        # Adjust window size and set minimum/maximum limits
        self.geometry("725x540")
        self.minsize(725, 540)
        self.maxsize(725, 540)

        ico = Image.open(os.path.join(dirname, 'icon.jpg'))
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(False, photo)

        # Set background color
        self.config(bg="#293241")

        # Load application image (assuming an image file named "DetImage.png" exists)
        self.app_image = tk.PhotoImage(file="DetImage.png")
        self.app_image_label = tk.Label(self, image=self.app_image)                 
        self.app_image_label.grid(row=0, column=0, padx=10, pady=30)

        # Create title label with custom styling
        self.title_label = customtkinter.CTkLabel(self,
                                                text_color="#EE6C4D",
                                                text="MATRIX DETERMINANT\nCALCULATOR",
                                                font=customtkinter.CTkFont(size=18))
        self.title_label.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # Create buttons for different matrix sizes
        self.calc_buttons = {}
        matrix_sizes = ["2x2", "3x3", "4x4", "5x5", "6x6", "7x7", "8x8", "9x9", "10x10"]
        self.grid_row = 2  # Track current row for grid placement
        self.grid_column = 0  # Track current column for grid placement

        for size in matrix_sizes:
            button_text = f"{size} Matrix"

            # Create a button with custom styling and functionality for opening the calculator for the chosen size
            button = customtkinter.CTkButton(master=self,
                                            text=button_text,
                                            command=lambda size=size: self.open_calculator(size),
                                            corner_radius=0,
                                            width=150,
                                            height=60,
                                            text_color="#EEEEEE",
                                            fg_color="#293241",
                                            hover_color="#EE6C4D",
                                            border_width=1,
                                            border_color="#EE6C4D",
                                            font=customtkinter.CTkFont(size=16,))

           # Place the button on the grid and alternate columns
            button.grid(row=self.grid_row, column=self.grid_column % 3, pady=5, padx=5)  
            self.calc_buttons[size] = button
            self.grid_column += 1  # Move to the next column for the next button

            # Check if a row is filled (2 buttons) and move to the next row if needed
            if self.grid_column == 3:
                self.grid_column = 0
                self.grid_row += 1

    def open_calculator(self, matrix_size):
        """
        Opens the appropriate calculator window based on the selected matrix size.

        Args:
            matrix_size (str): The size of the matrix (e.g., "2x2", "3x3").
        """

        # Create a MatrixCalculator object for the chosen size
        if matrix_size == "2x2":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=2)
        elif matrix_size == "3x3":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=3)
        elif matrix_size == "4x4":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=4)
        elif matrix_size == "5x5":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=5)
        elif matrix_size == "6x6":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=6)
        elif matrix_size == "7x7":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=7)
        elif matrix_size == "8x8":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=8)
        elif matrix_size == "9x9":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=9)
        elif matrix_size == "10x10":
            calculator = MatrixCalculator(self, size_desc=matrix_size, dim=10)
        else:
            print("Invalid matrix size selected.")  # Handle unexpected size
            return

        calculator.calculator_window.mainloop()  # Run the calculator's event loop

# Run the main application loop if this script is executed directly
if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()