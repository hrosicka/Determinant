from CTkMessagebox import CTkMessagebox

def show_error_message(message="Invalid matrix data. Enter numbers only."):
    return CTkMessagebox(title="Error",
                      message=message,
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
                      border_width=0,
                      #border_color="#3E4754"
                      )