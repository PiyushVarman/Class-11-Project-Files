from tkinter import *

root=Tk()
root.geometry("600x600")
root.resizable(False,False)
root.configure(bg='#FFD700')
Label(root,text="P",font=("Calibri",400),bg="#FFD700").place(x=300,y=250,anchor="center")
n=Entry(root,text='hi').pack()
root.mainloop()
