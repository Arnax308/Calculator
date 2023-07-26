from tkinter import *
import tkinter.messagebox
root = Tk()

ans = tkinter.messagebox.askquestion("Question1", "Do you like Coffee?")

if ans == 'yes':
    print('Here is some coffee')

root.mainloop()