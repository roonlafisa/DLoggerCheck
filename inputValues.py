from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *



def clicked():
# ----do an empty label check
#calculation:

  global value, lowerlimit, upperlimit

  value1 = float(txt1.get())
  lowerlimit1 = value1 - float(combo1.get())*value1/100
  upperlimit1 = value1 + float(combo1.get())*value1/100

  value2 = float(txt2.get())
  lowerlimit2 = value2 - float(combo2.get())*value2/100
  upperlimit2 = value2 + float(combo2.get())*value2/100

  value3 = float(txt3.get())
  lowerlimit3 = value3 - float(combo3.get())*value3/100
  upperlimit3 = value3 + float(combo3.get())*value3/100

  value4 = float(txt4.get())
  lowerlimit4 = value3 - float(combo4.get())*value4/100
  upperlimit4 = value3 + float(combo4.get())*value4/100

  value = [value1, value2, value3, value4]
  lowerlimit = [lowerlimit1, lowerlimit2, lowerlimit3, lowerlimit4]
  upperlimit = [upperlimit1, upperlimit2, upperlimit3, upperlimit4]

  messagebox.showinfo('Message', 'Complete')
  window.destroy()

  for i, val in enumerate(value):
    print ('The input no is {} and the value is {}'.format(i , val))
    checkRange(i, val)

def checkRange(index, num):
# using comaparision operator
   if lowerlimit[index] <= num <= upperlimit[index]:
      print('The value {} is in range ({}, {})'.format(num, lowerlimit[index], upperlimit[index]))
   else:
      print('The value {} is not in range ({}, {})'.format(num, lowerlimit[index], upperlimit[index]))


# complete code

window = Tk()
window.title("Input range for testing")
window.geometry('700x300')

# input 1
lbl1a = Label(window, text="Reference for input 1 ")
txt1 = Entry()
txt1.insert(END, '10')
txt1.pack()
lbl1b = Label(window, text="     Percentage range ")
combo1 = Combobox(window)
combo1['values']= (1, 5, 10, 15, 20)
combo1.current(1) #set the selected item

# input 2
lbl2a = Label(window, text="Reference for input 2 ")
txt2 = Entry()
txt2.insert(END, '100')
txt2.pack()
lbl2b = Label(window, text="     Percentage range ")
combo2 = Combobox(window)
combo2['values']= (1, 5, 10, 15, 20)
combo2.current(1) #set the selected item

# input 3
lbl3a = Label(window, text="Reference for input 3 ")
txt3 = Entry()
txt3.insert(END, '1000')
txt3.pack()
lbl3b = Label(window, text="     Percentage range ")
combo3 = Combobox(window)
combo3['values']= (1, 5, 10, 15, 20)
combo3.current(1) #set the selected item

# input 4
lbl4a = Label(window, text="Reference for input 4 ")
txt4 = Entry()
txt4.insert(END, '10000')
txt4.pack()
lbl4b = Label(window, text="     Percentage range ")
combo4 = Combobox(window)
combo4['values']= (1, 5, 10, 15, 20)
combo4.current(1) #set the selected item








# Placeholders:

lbl1a.grid(column=0, row=0)
txt1.grid(column=1, row=0)
lbl1b.grid(column=2, row=0)
combo1.grid(column=3, row=0)

lbl2a.grid(column=0, row=1)
txt2.grid(column=1, row=1)
lbl2b.grid(column=2, row=1)
combo2.grid(column=3, row=1)

lbl3a.grid(column=0, row=2)
txt3.grid(column=1, row=2)
lbl3b.grid(column=2, row=2)
combo3.grid(column=3, row=2)

lbl4a.grid(column=0, row=3)
txt4.grid(column=1, row=3)
lbl4b.grid(column=2, row=3)
combo4.grid(column=3, row=3)

#Button settings
btn = Button(window, text="Measure", command=clicked)
btn.grid(column=2, row=7)




window.mainloop()
