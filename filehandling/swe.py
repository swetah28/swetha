#open("swetha.txt","x")
win=open("swetha.txt","w")
for i in range(5):
    a=input("enter the name:")
    b=int(input("enter the age:"))
    c=input("enter the add:")
    i=a,b,c,
    print(i)
    win.write("name:"+a+"\n")
    win.write("age:"+str(b)+"\n")
    win.write("address:"+c+"\n")
    win.write("\n")
win.close()