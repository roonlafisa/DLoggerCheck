from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import math

def instructions():
    #instructions
    instruc = Toplevel(window)
    instruc.title("Results")
    instruc.geometry("600x200")
    lblins1 = Label(instruc, text="Step1: Input your reference data and select percentage tolerance range. Hit 'set tolerance'")
    lblins1.grid(column=0, row=1)
    lblins2 = Label(instruc, text="Step2: Input your input values and hit 'measure button'")
    lblins2.grid(column=0, row=3)

def set_tolerance():
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
  lowerlimit4 = value4 - float(combo4.get())*value4/100
  upperlimit4 = value4 + float(combo4.get())*value4/100

  value = [value1, value2, value3, value4]
  lowerlimit = [lowerlimit1, lowerlimit2, lowerlimit3, lowerlimit4]
  upperlimit = [upperlimit1, upperlimit2, upperlimit3, upperlimit4]

#  if (math.isnan(txt4.get())):
#      messagebox.showinfo('Message', 'error')
#      window.destroy()


def checkRange():
    global index, input, checkeddata
    checkeddata=["incorrect value", "incorrect value", "incorrect value", "incorrect value"]
    # set inputs
    testin1 = float(txtin1.get())
    testin2 = float(txtin2.get())
    testin3 = float(txtin3.get())
    testin4 = float(txtin4.get())
    input = [testin1, testin2, testin3, testin4]

    for index in range(len(input)):
        if lowerlimit[index] <= input[index] <= upperlimit[index]:
            checkeddata[index] = "value OK "
            print(index)
        else:

            continue

    newWindow = Toplevel(window)
    newWindow.title("Results")
    newWindow.geometry("200x200")
    lblout1a = Label(newWindow, text="Input 1: ",)
    lblout2a = Label(newWindow, text="Input 2: ")
    lblout3a = Label(newWindow, text="Input 3: ")
    lblout4a = Label(newWindow, text="Input 4: ")
    lblout1b = Label(newWindow, text=checkeddata[0])
    lblout2b = Label(newWindow, text=checkeddata[1])
    lblout3b = Label(newWindow, text=checkeddata[2])
    lblout4b = Label(newWindow, text=checkeddata[3])
    lblout1a.grid(column=1, row=0)
    lblout2a.grid(column=1, row=1)
    lblout3a.grid(column=1, row=2)
    lblout4a.grid(column=1, row=3)
    lblout1b.grid(column=2, row=0)
    lblout2b.grid(column=2, row=1)
    lblout3b.grid(column=2, row=2)
    lblout4b.grid(column=2, row=3)

    button = Button(newWindow, text = "Click and Quit", command = newWindow.destroy)
    button.grid(column=2, row=8)








# complete code

window = Tk()
window.title("Data Log QC Semi-Automation")
window.geometry('950x180')


# value 1
lbl1a = Label(window, text="Reference for input 1 ")
txt1 = Entry()
txt1.insert(END, '10')
txt1.pack()
lbl1b = Label(window, text="     Percentage tolerance ")
combo1 = Combobox(window)
combo1['values']= (1, 5, 10, 15, 20)
combo1.current(1) #set the selected item

# value 2
lbl2a = Label(window, text="Reference for input 2 ")
txt2 = Entry()
txt2.insert(END, '100')
txt2.pack()
lbl2b = Label(window, text="     Percentage tolerance ")
combo2 = Combobox(window)
combo2['values']= (1, 5, 10, 15, 20)
combo2.current(1) #set the selected item

# value 3
lbl3a = Label(window, text="Reference for input 3 ")
txt3 = Entry()
txt3.insert(END, '1000')
txt3.pack()
lbl3b = Label(window, text="     Percentage tolerance ")
combo3 = Combobox(window)
combo3['values']= (1, 5, 10, 15, 20)
combo3.current(1) #set the selected item

# value 4
lbl4a = Label(window, text="Reference for input 4 ")
txt4 = Entry()
txt4.insert(END, '10000')
txt4.pack()
lbl4b = Label(window, text="     Percentage tolerance ")
combo4 = Combobox(window)
combo4['values']= (1, 5, 10, 15, 20)
combo4.current(1) #set the selected item

# inputs
lblin1 = Label(window, text="     Input test value 1 ")
txtin1 = Entry()
txtin1.insert(END, '10')
txtin1.pack()
lblin2 = Label(window, text="     Input test value 2 ")
txtin2 = Entry()
txtin2.insert(END, '100')
txtin2.pack()
lblin3 = Label(window, text="     Input test value 3 ")
txtin3 = Entry()
txtin3.insert(END, '1000')
txtin3.pack()
lblin4 = Label(window, text="     Input test value 4 ")
txtin4 = Entry()
txtin4.insert(END, '10000')
txtin4.pack()



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

lblin1.grid(column=4, row=0)
txtin1.grid(column=5, row=0)
lblin2.grid(column=4, row=1)
txtin2.grid(column=5, row=1)
lblin3.grid(column=4, row=2)
txtin3.grid(column=5, row=2)
lblin4.grid(column=4, row=3)
txtin4.grid(column=5, row=3)

# instructionss
btnins = Button(window, text="instructions", command=instructions)
btnins.grid(column=1, row=7)

# set tolerance button
btn = Button(window, text="Set tolerance", command=set_tolerance)
btn.grid(column=2, row=7)

# checkrange button
btn2 = Button(window, text="Check data", command=checkRange)
btn2.grid(column=5, row=7)


#update results


window.mainloop()
