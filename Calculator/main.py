from tkinter import *
import ast
import math

# Color Scheme
DARK_BG = '#1a1a1a'
MEDIUM_BG = '#2d2d2d'
LIGHT_BG = '#3d3d3d'
TEXT_COLOR = '#ffffff'
BUTTON_COLOR_NUM = MEDIUM_BG
BUTTON_COLOR_OP = LIGHT_BG
BUTTON_COLOR_SPECIAL = '#ff9500'
BUTTON_COLOR_SCI = '#4a4a4a'

# Global variables
i = 0
history_list = []
history_visible = False

def get_number(num):
    global i
    display.insert(i, num)
    i += 1

def get_operations(oper):
    global i
    display.insert(i, oper)
    i += len(oper)

def all_clear():
    display.delete(0, END)

def calculate(*args):  # Added *args to handle both button and Enter key
    entire_str = display.get()
    try:
        env = {
            '__builtins__': None,
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'sqrt': math.sqrt,
            'log': math.log10,
            'ln': math.log,
            'pi': math.pi,
            'e': math.e,
            'radians': math.radians,
            'degrees': math.degrees,
        }
        node = ast.parse(entire_str, mode="eval")
        result = eval(compile(node, '<string>', "eval"), env)
        all_clear()
        display.insert(0, result)
        
        # Update history
        history_list.append(f"{entire_str} = {result}")
        if history_visible:
            update_history_display()
    except Exception as e:
        all_clear()
        display.insert(0, "Error")

def backspace():
    entire_str = display.get()
    if len(entire_str):
        new_str = entire_str[:-1]
        all_clear()
        display.insert(0, new_str)
    else:
        all_clear()
        display.insert(0, '')

def toggle_history():
    global history_visible
    history_visible = not history_visible
    if history_visible:
        history_display.grid()
        update_history_display()
    else:
        history_display.grid_remove()

def update_history_display():
    history_display.config(state=NORMAL)
    history_display.delete(1.0, END)
    history_display.insert(END, '\n'.join(history_list[-3:]))
    history_display.config(state=DISABLED)

# Create main window
root = Tk()
root.title("Scientific Calculator")
root.geometry('600x500')
root.configure(bg=DARK_BG)

# Bind Enter key to calculate function
root.bind('<Return>', calculate)

# Configure grid weights
for col in range(8):
    root.grid_columnconfigure(col, weight=1)
for row in range(7):
    root.grid_rowconfigure(row, weight=1)

# Display
display = Entry(root, font=('Arial', 24), bg=MEDIUM_BG, fg=TEXT_COLOR, 
                insertbackground=TEXT_COLOR, justify='right', borderwidth=0)
display.grid(row=0, column=0, columnspan=8, sticky='ew', padx=10, pady=10)
display.focus()  # Set focus to display for immediate keyboard input

# History Display (initially hidden)
history_display = Text(root, font=('Arial', 10), bg=MEDIUM_BG, fg=TEXT_COLOR, 
                      height=3, state=DISABLED, borderwidth=0)
history_display.grid(row=1, column=0, columnspan=8, sticky='ew', padx=10, pady=(0,10))
history_display.grid_remove()

# History Toggle Button
Button(root, text='History', font=('Arial', 12), bg=BUTTON_COLOR_SCI, fg=TEXT_COLOR,
       activebackground=LIGHT_BG, borderwidth=0, command=toggle_history
      ).grid(row=0, column=7, sticky='ne', padx=2, pady=2)

# Number buttons
numbers = [7, 8, 9, 4, 5, 6, 1, 2, 3]
counter = 0
for x in range(3):
    for y in range(3):
        button = Button(root, text=str(numbers[counter]), font=('Arial', 14), 
                       bg=BUTTON_COLOR_NUM, fg=TEXT_COLOR, activebackground=LIGHT_BG,
                       borderwidth=0, command=lambda num=numbers[counter]: get_number(num))
        button.grid(row=x+2, column=y, sticky='nsew', padx=2, pady=2)
        counter += 1

# Zero button
Button(root, text='0', font=('Arial', 14), bg=BUTTON_COLOR_NUM, fg=TEXT_COLOR,
       activebackground=LIGHT_BG, borderwidth=0, command=lambda: get_number(0)
      ).grid(row=5, column=1, sticky='nsew', padx=2, pady=2)

# Basic operations
basic_ops = ['+', '-', '×', '÷', '(', ')', '^', '%', 'π', 'e']
basic_commands = ['+', '-', '*', '/', '(', ')', '**', '%', 'math.pi', 'math.e']
for index, (op, cmd) in enumerate(zip(basic_ops, basic_commands)):
    Button(root, text=op, font=('Arial', 14), bg=BUTTON_COLOR_OP, fg=TEXT_COLOR,
           activebackground=LIGHT_BG, borderwidth=0, 
           command=lambda cmd=cmd: get_operations(cmd)
          ).grid(row=2 + index//3, column=3 + index%3, sticky='nsew', padx=2, pady=2)

# Scientific functions including square and cube
sci_ops = ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'x²', 'x³']
sci_commands = ['sin(', 'cos(', 'tan(', 'sqrt(', 'log10(', 'log(', '**2', '**3']
for index, (op, cmd) in enumerate(zip(sci_ops, sci_commands)):
    Button(root, text=op, font=('Arial', 12), bg=BUTTON_COLOR_SCI, fg=TEXT_COLOR,
           activebackground=LIGHT_BG, borderwidth=0,
           command=lambda cmd=cmd: get_operations(cmd)
          ).grid(row=2 + index//2, column=6 + index%2, sticky='nsew', padx=2, pady=2)

# Special buttons
Button(root, text='AC', font=('Arial', 14), bg=BUTTON_COLOR_SPECIAL, fg=TEXT_COLOR,
       activebackground='#ffaa33', borderwidth=0, command=all_clear
      ).grid(row=5, column=0, sticky='nsew', padx=2, pady=2)

Button(root, text='=', font=('Arial', 14), bg=BUTTON_COLOR_SPECIAL, fg=TEXT_COLOR,
       activebackground='#ffaa33', borderwidth=0, command=calculate
      ).grid(row=5, column=2, sticky='nsew', padx=2, pady=2)

Button(root, text='⌫', font=('Arial', 14), bg=BUTTON_COLOR_SPECIAL, fg=TEXT_COLOR,
       activebackground='#ffaa33', borderwidth=0, command=backspace
      ).grid(row=5, column=4, sticky='nsew', padx=2, pady=2)

# Decimal point
Button(root, text='.', font=('Arial', 14), bg=BUTTON_COLOR_NUM, fg=TEXT_COLOR,
       activebackground=LIGHT_BG, borderwidth=0, command=lambda: get_number('.')
      ).grid(row=5, column=5, sticky='nsew', padx=2, pady=2)

root.mainloop()
