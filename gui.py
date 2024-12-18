import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from lexer import lexer_action

background = "#303446"
foreground = "#d5cee3"
font = "#232634"
font_green = "green"
font_orange = "#ffaa2c"
font_red = "#ff5555"


def on_content_changed(event=None):
    update_line_numbers()
    sync_scrollbars()


def update_line_numbers():
    line_number_box.config(state="normal")
    line_number_box.delete("1.0", "end")

    content = text_box.get("1.0", "end-1c")

    if content:
        lines = content.split("\n")
        line_count = len(lines)

        line_numbers = "\n".join(str(i) for i in range(1, line_count + 1))
        line_number_box.insert("1.0", line_numbers)

    line_number_box.config(state="disabled")


def lex_text():
    try:
        text = text_box.get("1.0", "end-1c")
        token_list = lexer_action(text)
        display_tokens(token_list)
    except Exception as e:
        show_error_popup(str(e))


def display_tokens(token_list):
    new_window = tk.Toplevel(root)
    new_window.title("Tokens")
    new_window.configure(bg=f"{background}")
    style = ttk.Style()
    style.configure(
        "BW.TLabel",
        foreground=f"{foreground}",
        background=f"{background}",
        font=("Helvetica", 13),
    )

    tree = ttk.Treeview(
        new_window,
        columns=("Type", "Element", "Line"),
        show="headings",
        style="BW.TLabel",
    )
    tree.heading("Type", text="Tipo")
    tree.heading("Element", text="Elemento")
    tree.heading("Line", text="Linea")

    for token in token_list:
        tree.insert("", "end", values=(token[0], token[1], token[2]))

    tree.pack(expand=True, fill="both")


def import_file():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_box.delete("1.0", "end")
                text_box.insert("1.0", content)
                update_line_numbers()
    except Exception as e:
        show_error_popup(str(e))


def clear_content():
    text_box.delete("1.0", "end")
    update_line_numbers()


def exit_app():
    root.destroy()


def show_error_popup(message):
    error_popup = tk.Toplevel(root)
    error_popup.title("Error")
    error_popup.configure(bg=f"{background}")

    window_width = 600
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    error_popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    error_label = tk.Label(
        error_popup,
        text=message,
        bg=f"{background}",
        fg=f"{foreground}",
        font=("Consolas", 12),
    )
    error_label.pack(padx=10, pady=10)
    close_button = tk.Button(
        error_popup,
        text="De Acuerdo",
        command=error_popup.destroy,
        bg=f"{background}",
        fg=f"{foreground}",
        font=("Helvetica", 10),
    )
    close_button.pack(padx=10, pady=10)


def sync_scrollbars():
    line_number_box.yview_moveto(text_box.yview()[0])


root = tk.Tk()
root.title("Ruby Lexer")
root.configure(bg="#282a36")

window_width = 1280
window_height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

line_number_frame = tk.Frame(root, width=50, bg=f"{background}")
line_number_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

line_number_box = tk.Text(
    line_number_frame,
    width=4,
    padx=4,
    pady=4,
    wrap=tk.NONE,
    bg=f"{background}",
    fg=f"{foreground}",
    font=("Consolas", 13),
)
line_number_box.pack(side=tk.LEFT, fill=tk.Y)
line_number_box.config(state="disabled")

text_frame = tk.Frame(root, bg=f"{background}")
text_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

text_box = tk.Text(
    text_frame,
    height=40,
    width=100,
    bg=f"{background}",
    fg=f"{foreground}",
    font=("Consolas", 13),
)  # Set text box background color, text color, and font
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

text_box.bind("<Key>", on_content_changed)

button_frame = tk.Frame(root, bg=f"{background}")
button_frame.pack(side=tk.TOP, padx=10, pady=10)

lex_button = tk.Button(
    button_frame,
    text="Lexical Analysis",
    command=lex_text,
    width=10,
    height=2,
    fg=f"{font_green}",
    bd=0,
    font=("Helvetica", 12, "bold"),
)
lex_button.pack(side=tk.TOP, padx=5, pady=5)

import_button = tk.Button(
    button_frame,
    text="Import\nFile",
    command=import_file,
    width=10,
    height=2,
    bd=0,
    font=("Helvetica", 12, "bold"),
)
import_button.pack(side=tk.TOP, padx=5, pady=5)

clear_button = tk.Button(
    button_frame,
    text="Cleanup",
    command=clear_content,
    width=10,
    height=2,
    fg=f"{font_orange}",
    bd=0,
    font=("Helvetica", 12, "bold"),
)
clear_button.pack(side=tk.TOP, padx=5, pady=5)

exit_button = tk.Button(
    root,
    text="Exit!",
    command=exit_app,
    width=10,
    height=2,
    fg=f"{font_red}",
    bd=0,
    font=("Helvetica", 12, "bold"),
)
exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)


root.mainloop()
