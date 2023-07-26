from tkinter import *


def selected():
    sugar = sugar_var.get()
    ice = ice_var.get()
    cream = cream_var.get()

    if sugar:
        sugar = "Sugar"

    else:
        sugar = ''

    if ice:
        ice = "Ice"

    else:
        ice = ''

    if cream:
        cream = "Cream"

    else:
        cream = ''

    label.config(text="The selected options are: \n" + sugar + "\n" + ice + "\n" + cream)


root = Tk()
root.geometry("400x400")

sugar_var = BooleanVar()
ice_var = BooleanVar()
cream_var = BooleanVar()

sugar_chk = Checkbutton(root, text="Sugar", variable=sugar_var, command=selected)
ice_chk = Checkbutton(root, text="Ice", variable=ice_var, command=selected)
cream_chk = Checkbutton(root, text="Cream", variable=cream_var, command=selected)

label = Label(root)

sugar_chk.pack()
ice_chk.pack()
cream_chk.pack()
label.pack()

root.mainloop()
