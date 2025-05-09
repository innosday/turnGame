import tkinter as tk
from tkinter import *
from UntilFileJson import WriteJson

root = tk.Tk()

window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

center_width = int((window_width / 2) - 100)
center_height = int((window_height /2) - 40)

root.title("create_Object")
root.geometry(f"200x80+{center_width}+{center_height}")
root.resizable(False,False)

def save(select_ObjectType,):


def status():
    selected_var = var.get()

label_ObjectType = LabelFrame(root,text="오브젝트 타입")
label_ObjectType.pack(fill=BOTH,expand=True)

var = IntVar()
c1 = Radiobutton(label_ObjectType,text="Player",variable=var,value=1,command=status)
c2 = Radiobutton(label_ObjectType,text="Mob",variable=var,value=2,command=status)
c3 = Radiobutton(label_ObjectType,text="Object",variable=var,value=3,command=status)

c1.grid(row=1,column=1)
c2.grid(row=1,column=2)
c3.grid(row=1,column=3)

b1 = Button(root,text="확인",width=10,bg="yellow",command=)
b1.pack()

root.mainloop()
print("fd")