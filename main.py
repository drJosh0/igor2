'''
igor 2
Start Date: 2021 - 02 - 06


https://www.sec.gov/dera/data/financial-statement-data-sets.html
'''
import os
from tkinter import *


root = Tk()
root.title("IGOR V2.0 | TJC inc.")
root.geometry("800x600")

frame = Frame(root)
frame.pack(padx=5, pady=5, side=LEFT)

lbl1 = Label(frame, text="Welcome to IGOR") #: see datasets @ https://www.sec.gov/dera/data/financial-statement-data-sets.html")
lbl1.grid(column=0, row=0)

btnDownload = Button(frame, text="Download new DataSet")
btnDownload.grid(column=0, row=1)
#change


root.mainloop()