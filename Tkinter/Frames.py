from tkinter import *

root = Tk()

root.geometry("500x500")
frame1 = Frame(root,highlightthickness=2, highlightbackground="black", padx=30, pady=30)
frame1.pack()

frame2 = Frame(root)
frame2.pack(side=BOTTOM)

butt1 = Button(frame1, text="Button 1")
butt2 = Button(frame2, text="Button 2")

butt1.pack()
butt2.pack()

root.mainloop()