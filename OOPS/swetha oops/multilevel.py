class Hospital:
    def __init__(self,hospitalname,buildingnum,place):
        self.hospitalname=hospitalname
        self.buildingnum=buildingnum
        self.place=place
    def display(self):
        print("HOSPITAL DETAILS")
        print(f"hospitalname:{self.hospitalname}\nbuildingnum:{self.buildingnum}\nplace:{self.place}\n")
        print("DOCTORS DETAILS")
class doctors(Hospital):
    def __init__(self,hospitalname,buildingnum,place,name,expierence):
        super().__init__(hospitalname,buildingnum,place)
        self.name=name
        self.expierence=expierence
    def display1(self):
        super().display()
        print(f"name:{self.name}\nexpierence:{self.expierence}\n")
        print("PATIENT DETAILS")
class patient(doctors):
    def __init__(self,hospitalname,buildingnum,place,name,expierence,patientage,disease):
        super().__init__(hospitalname,buildingnum,place,name,expierence)
        self.patientage=patientage
        self.disease=disease
    def display2(self):
        super().display1()
        print(f"patientage={self.patientage}\ndisease={self.disease}\n")
        print("CHILDPATIENT DETAILS")
class childpatient(patient):
    def __init__(self,hospitalname,buildingnum,place,name,expierence,patientage,disease,roomno,stage):
        super().__init__(hospitalname,buildingnum,place,name,expierence,patientage,disease)
        self.roomno=roomno
        self.stage=stage
    def display3(self):
        super().display2()
        print(f"roomno:{self.roomno}\nstage:{self.stage}\n")
finish=childpatient("GRR Hospital",4,"chennai","senthil","20years",35,"Dengue",67,"firstlevel")
end=childpatient("mss hospital",23,"covai","raj","12years",67,"virus",4,"second level")
finish.display3()  
end.display3()



