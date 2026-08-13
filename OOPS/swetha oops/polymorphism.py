class animal:
    def __init__(self,pet,wild):
        self.pet=pet
        self.wild=wild
    def display(self):
        print("hi")
        print(f"pet:{self.pet}\t wild:{self.wild}")


class school:
    def __init__(self,matric,cbse):
        self.matric=matric
        self.cbse=cbse
    def display(self):
        print(f"matric:{self.matric}\t cbse:{self.cbse}")

class movie:
    def __init__(self,horror,comedy):
        self.horror=horror
        self.comedy=comedy
    def display(self):
        print(f"horror:{self.horror}\t comedy:{self.comedy}")
a=animal("dog","lion")
b=school("rotaryclub","target")
c=movie("kaanjurin","kalakalappu")
a.display()
b.display()
c.display()

'''class food:
    def __init__(self,lunch,dinner):
        self.lunch=lunch
        self.dinner=dinner
    def display(self):
        print("tasty")
        print(f"lunch:{self.lunch}\ndinner:{self.dinner}")

class party(food):
    def __init__(self,lunch,dinner,drinks):
        super().__init__(lunch,dinner)
        self.drinks=drinks
    def display(self):
        super().display()
        print(f"drinks:{self.drinks}")

a=party("biriyani","parrota","juice")
a.display()
 
class beach:
    def __init__(self,place,seafood):
        self.place=place
        self.seafood=seafood
    def display(self):
        print("wow")
        print(f"place:{self.place}\nseafood:{self.seafood}")
class mountain:
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"name:{self.name}")
a=beach("kaniyakumari","crab")
b=mountain("everest")
a.display()
b.display()
'''
'''class trys:
    def helo(self,a,b):
        x=a/b
        print(x)
    def hi(self,a,b,c):
        y=a+b+c
        print(y)
s=trys()
s.helo(10,5)
s.hi(10,20,20)'''
'''
class world:
    def rose(self,a,b):
        if a==b:
            return("ok")
        else:
            return("notok")
    def display(self):
        print("helo")
    def lily(self,a,b,c):
        y=a+b+c
        print(y) 
    def display1(self):
        print("hai")       
x=world()
print(x.rose(10,20))
x.lily(10,20,30)
x.display()
x.display1()'''

class arithmetic:
    def add(self,a,b):
        x=a+b
        print (x)
    def sub(self,a,b,c):
        y=(a+b)-c
        print(y)
    def display(self):
        print("hii")
class arith(arithmetic):
    def multi(self,a,b,s):
        super().display()
        m=(a+b)*s
        print(m)
    def div(self,a,b,c,l):
        n=c/l
        print(n)
    def display(self):
        print("helo")

f=arithmetic()
f.add(12,3)
f.sub(2,3,5)

h=arith()
h.multi(10,5,2)
h.div(3,1,10,2)
       


        


