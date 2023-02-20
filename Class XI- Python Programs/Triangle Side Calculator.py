from tkinter import *
from tkinter import messagebox
import math
root=Tk()
root.geometry("1226x579")
root.resizable(False,False)
root.configure(bg="#007F87")
bg_image =PhotoImage(file="rtriangle.png")
tri=Label(root,image=bg_image,bg="#007F87")
tri.place(x=300,y=250,anchor='center')
root.title("Triangle Side Calculator")
intro=Label(root,text="Triangle Side Calculator!",font=("Georgia",20,"bold italic"),bg="#007F87")
intro.place(x=613,y=50,anchor="center")
rules=Label(root,text="Enter any 2 lengths of the triangle\n and find the third!",font=("Georgia",15,"bold italic"),bg="#007F87")
rules.place(x=613,y=100,anchor="center")
def calculation():
    global root
    global Result
    Result.destroy()
    base=b.get().strip()
    height=a.get().strip()
    hypo=c.get().strip()
    if (base.isdigit() and height.isdigit()) or (base.isdigit() and hypo.isdigit()) or (height.isdigit() and hypo.isdigit()):
        if str(base).isdigit() and str(height).isdigit():
            base=int(base)
            height=int(height)
            res=math.hypot(base,height)
            fin="Hypotenuse is:\n"+str(res)
            Result=Label(root,text=fin,font=("Georgia",40,"italic"),bg="#007F87")
            Result.place(x=600,y=200)
        if str(base).isdigit() and str(hypo).isdigit():
            base=int(base)
            hypo=int(hypo)
            res=math.sqrt(hypo**2-base**2)
            fin="Height is:\n"+str(res)
            Result=Label(root,text=fin,font=("Georgia",40,"italic"),bg="#007F87")
            Result.place(x=600,y=200)
        if str(height).isdigit() and str(hypo).isdigit():
            height=int(height)
            hypo=int(hypo)
            res=math.sqrt(hypo**2-height**2)
            fin="Base is:\n"+str(res)
            Result=Label(root,text=fin,font=("Georgia",40,"italic"),bg="#007F87")
            Result.place(x=600,y=200)
    else:
        messagebox.showerror("Warning!","Input at least\n2 integer values for 2 sides")
Result=Result=Label(root,text="",font=("Georgia",40,"italic"),bg="#007F87")
Result.place(x=600,y=200)
a=Entry(root,font=("Arial",12,"bold"),width=5,justify="center")
a.place(x=50,y=250) #height
b=Entry(root,font=("Arial",12,"bold"),width=5,justify="center")
b.place(x=250,y=420) #base
c=Entry(root,font=("Arial",12,"bold"),width=5,justify="center")
c.place(x=300,y=220) #hypotenuse
g=Button(root,text="Calculate",font=("Georgia",12,"bold italic"),bg="#00FF00",activebackground='#FFFF00',command=calculation)
g.place(x=225,y=460)
