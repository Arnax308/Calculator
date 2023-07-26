from tkinter import *
import ast

i = 0


def get_number(num):
    # using global to connect i in main and i in function
    global i

    display.insert(i, num)
    # insert has 2 parameters index and the value, so i starts with 0,
    # and will inc once we enter a num.
    # i will inc, once a value is inserted

    i += 1


def get_operations(oper):
    # Using the global i, it would alr have index of numbers inserted
    # This will allow the operator to be placed directly after the numbers
    global i
    display.insert(i, oper)

    # Not all the operators are of 1 char, hence using the len of the operator
    i += len(oper)


def all_clear():
    display.delete(0, END)


def calculate():
    entire_str = display.get()

    try:
        node = ast.parse(entire_str, mode="eval")
        result = eval(compile(node, '<string>', "eval"))
        all_clear()
        display.insert(0, result)

    except Exception:
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


root = Tk()

display = Entry(root)
display.grid(row=1, columnspan=6)

# Adding Buttons for numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
counter = 0

for x in range(3):
    for y in range(3):
        # Can discard the use of variable button_text, but it inc code readability
        button_text = numbers[counter]

        button = Button(text=button_text, height=2, width=4, command=lambda text=button_text: get_number(text))
        # Using text as a parameter to store the value of the current loop number
        # If we don't save the value local value of a loop in text, everytime, and directly pass in button_text
        # We will get 9, regardless of the button we press
        # This is because button_text we will get the last value after the loop, which is 9

        button.grid(row=x + 2, column=y)
        # x+2 because the first row is empty and the second one is used by display

        counter += 1

button0 = Button(text="0", height=2, width=4, command=lambda: get_number(0))
button0.grid(row=5, column=1)

# Adding Buttons for operators
operations = ["+", '-', '*', '/', '**', '%', '(', '**2', ')', '*3.14']

count = 0
for x in range(4):
    for y in range(3):

        if count < len(operations):
            button = Button(root, text=operations[count], height=2, width=4, command=lambda text=operations[count]: get_operations(text))
            button.grid(row=x + 2, column=y + 3)
            # y+3 because we have added numbers in a grid of 3x3, hence to not overlap them
            count += 1

# Adding Button for All Clear
Button(root, text="AC", height=2, width=4, command=all_clear).grid(row=5, column=0)

# Adding Button for =
Button(root, text="=", height=2, width=4, command=calculate).grid(row=5, column=2)

# Adding Button for backspace
Button(root, text="<-", height=2, width=4, command=backspace).grid(row=5, column=4)
root.mainloop()
