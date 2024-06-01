import customtkinter

def create_calculation_button(window, text, command):
    """
    This function creates a custom button with the specified parameters
    for triggering calculations.

    Args:
        window (customtkinter.CTk): The window where the button will be placed.
        text (str): The text displayed on the button.
        command (function): The function to be called when the button is clicked.

    Returns:
        customtkinter.CTkButton: The created button object.
    """

    # Create a CTkButton object with the following parameters:
    button = customtkinter.CTkButton(master=window,
                        text=text,
                        command=command,
                        corner_radius=0,
                        width=100,
                        height=40,
                        text_color="#EEEEEE",
                        fg_color="#293241",
                        hover_color="#EE6C4D",
                        border_width=1,
                        border_color="#EE6C4D",
                        font=customtkinter.CTkFont(size=12,))
    
    # Return the created button object
    return button