from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.geometry("500x500")
root.resizable(False,False)
root.configure(bg="#FFD700")
root.title("Guess the Number!")

def guess(event):
    global result
    global choice
    choice.destroy()
    result.destroy()
    play=g.get()
    if play.isdigit() and 0<=int(play)<=10:
        cpu=random.randrange(1,11)
        choice=Label(root,text=cpu,font=("Consolas",100,"bold"),bg="#FFD700")
        choice.place(x=250,y=185,anchor="center")
        if int(play)==cpu:
            result=Label(root,text="You Win!",font=("Calbri",25,"italic"),fg='green',bg="#FFD700")
            result.place(x=250,y=310,anchor="center")
        else:
            result=Label(root,text="You Lose!",font=("Calbri",25,"italic"),fg='red',bg="#FFD700")
            result.place(x=250,y=310,anchor="center")
    else:
        messagebox.showerror("Hold on!","The input should be\na number from 1 to 10!")
    g.delete(0,END)
Rule=Label(root,text="Enter a number from 1 to 10.\nSee if you got it right!",font=("Consolas",20),bg="#FFD700")
Rule.place(x=250,y=50,anchor="center")
result=Label(root,text="",font=("Calbri",25,"italic"),fg='green',bg="#FFD700")
result.place(x=250,y=300,anchor="center")
choice=Label(root,text="",font=("Calibri",50),bg="#FFD700")
choice.place(x=250,y=150,anchor="center")
g=Entry(root,font=("Georgia",15))
g.place(x=250,y=400,anchor="center")
b=Button(root,text="Guess!",font=("Consolas",12,"bold"),command=guess,bg="#39FF14",activebackground='red',borderwidth=2)
b.place(x=250,y=460,anchor="center")
root.bind('<Return>',guess)
