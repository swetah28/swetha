'''class arithmetic:
    def __init__(self,add,sub):
        self.__add=add
        self.__sub=sub
    def gettermul(self):
        return self.__add
        return self.__sub 
    def setterdiv(self,div):
        self.__div=div 
a=arithmetic(2+4,3-1)
print(a.gettermul())
a.setterdiv(10/2)
print(a.gettermul())'''

'''class student:
    def __init__(self,name,place,age):
        self.name=name
        self.__place=place
        self.__age=age
    def getterplay(self):
        return self.__place
    def getterplay1(self):
        return self.__age
    def setterplay(self,age):
        self.__age=age
a=student("swetha","chennai",23)
print(a.name)
a.setterplay(24)
print(a.getterplay())
print(a.getterplay1())'''

class bird:
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
    def getterplay(self):
        return self.__name
    def getterplay1(self):
        return self.__color
    def setterplay(self,color):
        self.__color=color
a=bird("parrot","green")
print(a.getterplay())
a.setterplay("red")
print(a.getterplay1())



