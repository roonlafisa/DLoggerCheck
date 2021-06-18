from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
def clicked():
    # ----do an empty label check

    #calculation
    value = float(txt1.get())
    lowerlimit = value - float(combo1.get())*value/100
    upperlimit = value + float(combo1.get())*value/100
    #print(value)
    #print(lowerlimit)
    #print(upperlimit)
    # return
    return input, lowerlimit, upperlimit
    #
    messagebox.showinfo('Message title', 'Message content')



window = Tk()
window.title("Input range for testing")
window.geometry('550x200')

# input 1
lbl = Label(window, text="Input 1 value ")
lbl.grid(column=0, row=0)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=0)
lbl = Label(window, text="     Percentage range ")
lbl.grid(column=2, row=0)
combo1 = Combobox(window)
combo1['values']= (1, 5, 10, 15, 20)
combo1.current(1) #set the selected item
combo1.grid(column=3, row=0)



#Button settings
btn = Button(window, text="Measure", command=clicked)
btn.grid(column=2, row=1)



window.mainloop()
