import tkinter as tk 
from tkinter import *

import math

win = tk.Tk()
win.title("Trangle Area Calculator")
win.geometry("600x200")

eoutput = StringVar()
eoutput.set("insufficient conditoins")

l1=tk.Label(win,text=" Enter side 1: ")
l2=tk.Label(win,text=" Enter side 2: ")
l3=tk.Label(win,text=" Enter side 3: ")
l4=tk.Label(win,text=" Enter height: ")
l5=tk.Label(win,text=" Enter base: ")
l6=tk.Label(win,text=" Do you know the base and height? ")
l7=tk.Label(win,text=" Do you know the length of the 3 sides? ")

l8=tk.Label(win,text=" Area: ")

e1=tk.Entry(win,width=10)
e2=tk.Entry(win,width=10)
e3=tk.Entry(win,width=10)
e4=tk.Entry(win,width=10)
e5=tk.Entry(win,width=10)

e6=tk.Entry(win,width=20, textvariable=eoutput)

def step1():
    l1.grid(row=2,column=1)
    e1.grid(row=2,column=2)
    l2.grid(row=2,column=3)
    e2.grid(row=2,column=4)
    l3.grid(row=2,column=5)
    e3.grid(row=2,column=6)
    b5.grid(row=3,column=1,columnspan=2)

def step2():
    l6.grid(row=2,column=1)
    b3.grid(row=2,column=2)
    b4.grid(row=2,column=3)

def step3():
    l4.grid(row=3,column=1)
    e4.grid(row=3,column=2)
    l5.grid(row=3,column=3)
    e5.grid(row=3,column=4)
    b6.grid(row=4,column=1,columnspan=2)    

def step4():
    l8.grid(row=5,column=3)
    e6.grid(row=5,column=4)
    answer="cannot calculate"
    e6.delete(0,END)
    e6.insert(0,answer)

def calculate_1():
    l8.grid(row=5,column=3)
    e6.grid(row=5,column=4)
    answer=""
    num1 = e1.get()
    num2 = e2.get()
    num3 = e3.get()
    if num1.isdigit() and num2.isdigit() and num3.isdigit():
        num1=float(num1)
        num2=float(num2)
        num3=float(num3)
        s=float((num1+num2+num3)/2)
        c=math.sqrt(s*(s-num1)*(s-num2)*(s-num3))
    else:
        c='insufficient conditoins'

    answer=str(c)

    e6.delete(0,END)
    e6.insert(0,answer)    

def calculate_2():
    l8.grid(row=5,column=3)
    e6.grid(row=5,column=4)
    answer="" 
    num1 = e4.get()
    num2 = e5.get()
    if num1.isdigit() and num2.isdigit():
        num1=float(num1)
        num2=float(num2)
        c=(num1*num2)/2
    else:
        c='insufficient conditions'
    answer=str(c)
    e6.delete(0,END)
    e6.insert(0,answer)    

b1 = tk.Button(win, text="Yes",command=step1)
b2 = tk.Button(win, text="No ",command=step2)
b3 = tk.Button(win, text="Yes",command=step3)
b4 = tk.Button(win, text="No ",command=step4)
b5 = tk.Button(win, text="Calculate",command=calculate_1)
b6 = tk.Button(win, text="Calculate",command=calculate_2)

l7.grid(row=1,column=1)
b1.grid(row=1,column=2)
b2.grid(row=1,column=3)


win.mainloop()
