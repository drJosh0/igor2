'''
igor 2
Start Date: 2021 - 02 - 06


'''
import os
from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("IGOR 2.0")
root.geometry("800x600")

############################# MENU BAR ###################################
menubar = Menu(root)
# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Cut', command=None)
edit.add_command(label='Copy', command=None)
edit.add_command(label='Paste', command=None)
edit.add_command(label='Select All', command=None)
edit.add_separator()
edit.add_command(label='Find...', command=None)
edit.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)
############################# MENU BAR ###################################

progress = Progressbar(root, orient = HORIZONTAL, length = 700, mode = 'determinate')
progress.pack(pady=10)

######## FRAME ########
frame1 = Frame(root)#, bd=10, bg='red')

lbl1 = Label(frame1, text="Company Name") #: see datasets @ https://www.sec.gov/dera/data/financial-statement-data-sets.html")
lbl1.grid(column=0, row=0, padx=10)
T1 = Entry(frame1)
T1.grid(column=1, row=0, padx=10)
btn1 = Button(frame1, text="Stuff")
btn1.grid(column=2, row=0, padx=10)

lbl2 = Label(frame1, text="Report Type")
lbl2.grid(column=0, row=1, padx=10, pady=10)
T2 = Entry(frame1)
T2.grid(column=1, row=1, padx=10, pady=10)
btn2 = Button(frame1, text="Stuff")
btn2.grid(column=2, row=1, padx=10, pady=10)

lbl3 = Label(frame1, text="Year Range (YYYY-YYYY)")
lbl3.grid(column=0, row=2, padx=10)
T3 = Entry(frame1)
T3.grid(column=1, row=2, padx=10)
btn3 = Button(frame1, text="Stuff")
btn3.grid(column=2, row=2, padx=10)

frame1.pack(padx=5, pady=5)
######## FRAME ########


frame2 = Frame(root)
btn4 = Button(frame2, text="SEARCH")
btn4.pack(padx=5, pady=5)
frame2.pack(padx=5, pady=5)



root.config(menu = menubar)
root.mainloop()