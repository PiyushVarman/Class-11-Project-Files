from tkinter import *
from tkinter import messagebox
import math
from fractions import Fraction as fr


root=Tk()  
root.geometry("600x600")
root.resizable(False,False)
root.configure(bg='#FFD700')
root.title("Permutation Calculator")
def permutations():
    n=a.get()
    r=b.get()
    n.strip()
    r.strip()
    if n.isdigit() and r.isdigit():
        n=int(n)
        r=int(r)
        nfac=math.factorial(n)
        nrfac=math.factorial(n-r)
        messagebox.showinfo("Result",fr(nfac/nrfac))
Label(root,text="P",font=("Calibri",400),bg="#FFD700").place(x=300,y=250,anchor="center")
a=Entry(root,width=4,justify=CENTER,font=("Calibri",50))
a.place(x=50,y=100)
b=Entry(root,width=4,justify=CENTER,font=("Calibri",50))
b.place(x=350,y=375)
b1=Button(text="GO!",command=permutations)
b1.place(x=500,y=200)
root.mainloop()
