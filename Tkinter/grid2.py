from tkinter import *

root = Tk()
root.geometry("400x400")

for x in range(3):
    for y in range(3):
        frame = Frame(root)
        frame.grid(row=x, column=y)

        button = Button(frame, text=f"Row{x}\nColumn{y}")
        button.pack(padx=20, pady=20)

root.mainloop()