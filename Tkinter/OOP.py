from tkinter import *


class Demo:

    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.but1 = Button(frame, text="Click Here", command=self.printmsg)
        self.but1.pack()

        self.label = Label(rootone)
        self.label.pack()

        self.but2 = Button(frame, text="Quit", command=frame.quit)
        self.but2.pack()

    def printmsg(self):
        self.label.config(text="Button Clicked")


root = Tk()
d = Demo(root)

root.mainloop()
