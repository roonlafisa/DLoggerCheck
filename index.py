from Tkinter import *

root = Tk()
x = IntVar()


def test():
    global x
    x.set(x.get() + 1)

label_1 = Label(root, text=x.get(), textvariable = x)
button_1 = Button(root, text='Click', command=test)
button_1.grid(row=0, column=0)
label_1.grid(row=0, column=1)

root.mainloop()
