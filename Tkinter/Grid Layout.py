from tkinter import *

root = Tk()
root.geometry("400x400")

name = Label(root, text="Password")
email = Label(root, text="Email")

name_e = Entry(root)
email_e = Entry(root)

button = Button(root, text="Login")

name.grid(row=1, column=0)
email.grid(row=0, column=0)

name_e.grid(row=1, column=1)
email_e.grid(row=0, column=1)

button.grid(row=2,column=1)
root.mainloop()