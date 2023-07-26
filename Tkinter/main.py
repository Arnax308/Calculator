from tkinter import *


def sel():
    label.config(text=chk_val.get())


root = Tk()
root.geometry("300x300")

chk_val = BooleanVar()
chkbtn = Checkbutton(root, text="Accept Terms", variable=chk_val, command=sel)
chkbtn.pack()

label = Label(root)
label.pack()

root.mainloop()
