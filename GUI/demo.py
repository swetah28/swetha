'''from tkinter import *

root=Tk()
root.title("MY GUI")
root.geometry("450x350")

l=Label(root,text="Hi! Hello. Welcome to My GUI")
l.grid(row=0,column=0)
l1=Label(root,text="FDGHFGJHNFJ")
l1.grid(row=0,column=1)
f=Frame(root,background="blue",height="100",width="100")
f.grid(row=1,column=0)
root.mainloop()
from tkinter import *
some=Tk()
some.title("Table")
some.geometry("500x500")
color=["red","orange","yellow","black","brown","blue","purple","violet","pink","green"]
for i in color:
    a=Frame(some,background=i,height="50",width="50")
    a.pack()
some.mainloop()


#####################################################################################################


from tkinter import *
way=Tk()
way.title("The World")
way.geometry("400x400")
color=["red" ,"orange","yellow"]
for i in color:
    a=Frame(way,background=i,height="300",width="300")
    a.pack()
way.mainloop()


########################################################################################################

from tkinter import *
root=Tk()
root.title("Button")
root.geometry("400x400")

l=Label(root,text="Name :")
l.place(x=450,y=200)

e=Entry(root)
e.place(x=500,y=200)

def save():
    a=e.get()
    print(a)

b=Button(root,text="Click",command=save)
b.place(x=500,y=300)

root.mainloop()

#################################################################################################


from tkinter import *
from tkinter import messagebox
wall=Tk()
wall.title("Details")
wall.geometry("800x800")
a=Label(wall,text="Biodata")
a.pack(padx="50",pady="30")

c=Entry(wall)
c.pack(padx=20,pady=40)

var=IntVar()

r=Radiobutton(wall,variable=var,value=1,text="male")
r.place(x=100,y=80)
r1=Radiobutton(wall,variable=var,value=2,text="Female")
r1.place(x=200,y=80)
def hlo():
    x=c.get()
    y=var.get()
    print("Name :",x)
    if y==1:
        print("Gender: Male")
    elif y==2:
        print("Gender: Female")
    else:
        messagebox.showerror("ERROR","Please select your Gender")
                                                                                                         
b=Button(text="Click",command=hlo)
b.pack()
wall.mainloop()

#########################################################################################################

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
rose=Tk()
rose.title("Form")
rose.geometry("1000x1000")
state=["Andhra","Mysore","Gujarat","Tamilnadu","Kerala"]
l=Label(rose,text="REGISTER  FORM")
l.pack(padx="100",pady="50")
s=Label(rose,text="Name  :")    
s.place(x=590,y=200)
e1=Entry(rose)
e1.place(x=650,y=200)
s1=Label(rose,text="Email  :")
s1.place(x=595,y=240)
e2=Entry(rose)
e2.place(x=650,y=240)
s2=Label(rose,text="Gender   :")
s2.place(x=590,y=280)
var=IntVar()
r=Radiobutton(rose,variable=var,value=1,text="Male")
r.place(x=670,y=280)
r1=Radiobutton(rose,variable=var,value=2,text="Female")
r1.place(x=750,y=280)
s4=Label(rose,text="Languages :")
s4.place(x=580,y=320)
var1=IntVar()
c1=Checkbutton(rose,variable=var1,text="C#")
c1.place(x=670,y=320)
var2=IntVar()
c2=Checkbutton(rose,variable=var2,text="Java")
c2.place(x=750,y=320)
var3=IntVar()
c3=Checkbutton(rose,variable=var3,text="Python")
c3.place(x=820,y=320)
var4=IntVar()
c4=Checkbutton(rose,variable=var4,text=".Net")
c4.place(x=900,y=320)
l5=Label(rose,text="State :")
l5.place(x=600,y=360)
y=ttk.Combobox(rose,values=state)
y.place(x=650,y=360)
y.set(state[2])
s3=Label(rose,text="phone  :")
s3.place(x=590,y=400)
e3=Entry()
e3.place(x=650,y=400)
def flower():
    c=e1.get()
    a=e2.get()
    f=e3.get()
    x=var.get()
    m1=y.get()
    print("Name  :", c)
    print("Email :", a)
    if x==1:
        print("Gender: male")
    elif x==2:
        print("Gender: female")
    else:
         messagebox.showerror("ERROR","please  select your Gender")
    v=var1.get(),var2.get(),var3.get(),var4.get()
    if v==(1,0,0,0):
        print("Language: c#")
    elif v==(0,1,0,0):
        print("Language : Java")
    elif v==(1,0,1,1):
        print("Lnaguage : Python")
    elif v==(0,0,0,1):
        print("Language : .Net")
    else:
        messagebox.showwarning("WARNING","please select your language")
    print("Phono :",f)
    print("state :", m1 )                                                               
    
b=Button(rose,text="Click" ,command=flower)
b.place(x=700,y=500)
rose.mainloop()

###############################################################################################

from tkinter import *
from tkinter import ttk
way=Tk()
way.title("BIODATA")
way.geometry("2000x2000")
option=["Gujarat","Andhra","punjab","kerala","tamilandu","pondichery"]
a=ttk.Combobox(way,values=option) 
a.pack(padx=10,pady=10)
def sum(): 
    s=a.get()
    print(s)
b=Button(way,text="Click",command=sum)
b.pack()
a.set(option[3])
way.mainloop()
 ###################################################################################################



from tkinter import *
from PIL import Image,ImageTk
root=Tk()
root.title("the picture")
root.geometry("500x400")
bg_image=Image.open("k.jpeg")
bg_photo=ImageTk.PhotoImage(bg_image.resize((500,400)))
bg_label=Label(root,image=bg_photo)
bg_label.place(x=500,y=120)
c=Button(root,text="Click")
c.place(x=680,y=380)
root.mainloop()

import tkinter as tk

from PIL import Image, ImageTk


root = tk.Tk()
root.title("Register Page with Image") 
root.geometry("500x400")

# Load background image
bg_image = Image.open("k.jpeg")  # Replace with your image file
bg_photo = ImageTk.PhotoImage(bg_image.resize((500, 400)))

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=123, y=321)

root.mainloop()
'''

import tkinter as tk 
import PIL as Image,ImageTk
root=tk.Tk()
root.title("The Picture")
root.geometry("1200x1200")
a=tk.Image.open("s.jpeg")
b=ImageTk.PhotoImage(a.resize((500,300)))
l=tk.Label(root,image=b)
l.place(x=500,y=120)
def pic():
    print("The college :Annamalai University")
c=tk.Button(root,text="Click",command=pic)
c.place(x=740,y=395)
root.mainloop()