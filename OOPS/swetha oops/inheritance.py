'''class car:
    def __init__(type,name):
        type.name=name
    def display(type):
        print(f"Name:{type.name} ")
class brand(car):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def display1(self):
        super().display()
        print(f"Color:{self.color}")
a=brand("Toyota","Blue")
a.display1()'''

'''class language:
    def __init__(type,Tamil,English,maths):
        type.tamil=Tamil
        type.english=English
        type.maths=maths
    def display(type):
        print(f"tamil:{type.tamil}")
        print(f"english:{type.english}")
        print(f"maths:{type.maths}")
class major(language):
    def __init__(self,Tamil,English,maths,chemistry):
        super().__init__(Tamil,English,maths)
        self.chemistry=chemistry
    def display1(self):
        super().display()
        print(f"chemistry:{self.chemistry}")
class alied(major):
    def __init__(selfs,Tamil,English,maths,chemistry,physics):
        super().__init__(Tamil,English,maths,chemistry)
        selfs.physics=physics
    def display2(selfs):
        super().display1()
        print(f"physics:{selfs.physics}")
a=alied(90,91,92,93,94 )
a.display2()'''
    
'''class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name:{self.name}\nage:{self.age}")
class work(student):
    def __init__(bio,name,age,exp):
        super().__init__(name,age)
        bio.exp=exp
    def display1(bio):
        super().display()
        print(f"exp:{bio.exp}")
a=work("swetha",20,"5years")
a.display1()'''
'''class person:
    def __init__(det,name,age,place):
        det.name=name
        det.age=age
        det.place=place
        print("person details\n")
    def display(det):
         print(f"name:{det.name}\nage:{det.age}\nplace:{det.place}\n")
         print("school details\n")
class school(person):
    def __init__(self,name,age,place,schlname,totalmark):
        super().__init__(name,age,place)
        self.schlname=schlname
        self.totalmark=totalmark
    def display1(self):
        super().display()
        print(f"schlname:{self.schlname}\ntotalmark:{self.totalmark}\n")
        print("college details\n")
class college(school):
    def __init__(bio,name,age,place,schlname,totalmark,clgname,department,year,rank):
        super().__init__(name,age,place,schlname,totalmark)
        bio.clgname=clgname
        bio.department=department
        bio.year=year
        bio.rank=rank
    def display2(bio):
        super().display1()
        print(f"clgname:{bio.clgname}\ndepartment:{bio.department}\nyear:{bio.year}\nrank:{bio.rank} ")
a=college("swetha",20,"myld","st.pauls",545,"daacollege","cs",2023,"distinct")
a.display2()'''

'''#open("try.txt","x")
class Details:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        sun=open("try.txt","a")
        sun.write(f"name:{self.name}\nage:{self.age}\naddress:{self.address}")
class extra(Details):
    def __init__(self,name,age,address,gender,education):
        super().__init__(name,age,address)
        self.gender=gender
        self.education=education
    def display1(self):
        sun=open("try.txt","a")
        super().display()
        sun.write(f"gender:{self.gender}\neducation:{self.education}")
a=extra("Anu",23,"Myld","Female","Degree completed")
a.display1()'''
'''
#open("try.txt","x")
class company:
    def __init__(self,companyname,place,workers,years):
        self.companyname=companyname
        self.place=place
        self.workers=workers
        self.years=years
    def display(self):
        moon=open("try.txt","a")
        moon.append(f"companyname:{self.companyname}\nplace:{self.place}\nworkers:{self.workers}\nyears:{self.years}")
class worker(company):
    def __init__(self,salary,age):'''

class family:
    def rose(self,a,b):
        x=a+b
        print(x) 
    def pink(self,a,b,c):
        y=a*b*c
        print(y) 
class friends(family):
    def red(self,a,b,c,d,e):
        super().rose(a,b)
        m=a+b+c+d+e
        print(m) 
    def orange(self,a,b,c,f,g):
        super().pink(a,b,c)
        n=a+b+c+f+g
        print(n) 
a=friends()
a.red(10,5,3,6,7)
a.orange(12,1,1,1,1)

         

