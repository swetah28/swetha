from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("The Picture")
root.geometry("1200x1200")
a=Image.open("j.jpeg")
b=ImageTk.PhotoImage(a.resize((500,400)))
l=Label(root,image=b)
l.place(x=20,y=10,relwidth=1,relheight=1)
c=Button(root,text="Click")
c.pack()
root.mainloop()

