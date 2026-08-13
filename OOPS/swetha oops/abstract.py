'''from abc import ABC, abstractmethod
class person(ABC):
    def __init__(self,name,place):
        self.name=name
        self.place=place
    @abstractmethod
    def dislay(self):
        print(f"Name:{self.name} Place:{self.place}")
class school(person):
    def __init__(self, name, place,score):
        super().__init__(name, place)
        self.score=score
    def dislay(self):
        super().dislay()
        print(f"Score:{self.score}")
a=school("Swetha","Myd",550)
a.dislay()'''

from abc import ABC, abstractmethod
class movie:
    def __init__(self,title,year):
        self.title=title
        self.year=year
    def display(self):
        print("wow")
        print(f"the title:{self.title}\nthe year:{self.year}")
class hero(movie):
    def __init__(self,title,year,name,age):
        super().__init__(title,year)
        self.name=name
        self.age=age
    @abstractmethod
    def dislay(self):
        super().display()
        print("ohh")
        print(f"name:{self.name}\nage:{self.age}")
class heroine(hero):
    def __init__(self,title,year,name,age,hname,hage):
        super().__init__(title,year,name,age)
        self.hname=hname
        self.hage=hage
    def dislay(self):
        super().dislay()
        print("hey")

c=heroine("gilli",2005,"vijay",30,"trisha",28)
print(c)
c.dislay()



    