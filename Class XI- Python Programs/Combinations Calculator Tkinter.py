from tkinter import *
from tkinter import messagebox
import math
from fractions import Fraction as fr


root=Tk()  
root.geometry("600x600")
root.resizable(False,False)
root.configure(bg='cyan')
root.title("Combinations Calculator")
def combinations():
    n=a.get()
    r=b.get()
    n.strip()
    r.strip()
    if n.isdigit() and r.isdigit():
        n=int(n)
        r=int(r)
        nfac=math.factorial(n)
        nrfac=math.factorial(n-r)
        rfac=math.factorial(r)
        messagebox.showinfo("Result",fr(nfac/(nrfac*rfac)))
Label(root,text="C",font=("Calibri",400),bg="cyan").place(x=300,y=250,anchor="center")
a=Entry(root,width=4,justify=CENTER,font=("Calibri",50))
a.place(x=50,y=100)
b=Entry(root,width=4,justify=CENTER,font=("Calibri",50))
b.place(x=450,y=375)
b1=Button(text="GO!",command=combinations)
b1.place(x=300,y=500)
root.mainloop()
