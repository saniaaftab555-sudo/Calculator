import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)

# Entry field
expression = ""

input_text = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=input_text,
    font=("Arial", 24),
    bd=10,
    insertwidth=2,
    width=14,
    borderwidth=4,
    justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)


# Functions
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)


def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""


def clear():
    global expression
    expression = ""
    input_text.set("")


def backspace():
    global expression
    expression = expression[:-1]
    input_text.set(expression)


# Button creator
def create_button(text, row, col, command):
    button = tk.Button(
        root,
        text=text,
        padx=20,
        pady=20,
        font=("Arial", 18),
        command=command
    )
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)


# Number buttons
create_button("7", 1, 0, lambda: press(7))
create_button("8", 1, 1, lambda: press(8))
create_button("9", 1, 2, lambda: press(9))
create_button("/", 1, 3, lambda: press("/"))

create_button("4", 2, 0, lambda: press(4))
create_button("5", 2, 1, lambda: press(5))
create_button("6", 2, 2, lambda: press(6))
create_button("*", 2, 3, lambda: press("*"))

create_button("1", 3, 0, lambda: press(1))
create_button("2", 3, 1, lambda: press(2))
create_button("3", 3, 2, lambda: press(3))
create_button("-", 3, 3, lambda: press("-"))

create_button(".", 4, 0, lambda: press("."))
create_button("0", 4, 1, lambda: press(0))
create_button("=", 4, 2, equal)
create_button("+", 4, 3, lambda: press("+"))

create_button("C", 5, 0, clear)
create_button("⌫", 5, 1, backspace)

# Make grid responsive
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run app
root.mainloop()
