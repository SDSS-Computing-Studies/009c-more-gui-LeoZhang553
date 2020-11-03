import tkinter as tk 
from tkinter import *

import math

win = tk.Tk()
win.title("Trangle Area Calculator")
win.geometry("600x200")


b1 = tk.Button(win, text="Yes",command=step1)
b2 = tk.Button(win, text="No ",command=step2)
l1=tk.Label(win,text='n')
l1=tk.Label(win,text='fd')
e1=tk.Entry(win,width=20)

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
e1.grid(row=3,column=1)

def step1():
    yo="nononono"
    e1.insert(0,yo)

def step2():
    l7.grid(row=2,column=1, columnspan=2)