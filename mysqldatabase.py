import pymysql as star;
database=star.connect(host="localhost",user="root",password="livewire")
cursorobj=database.cursor()
#cursorobj.execute("create database festival")
add=star.connect(host="localhost",user="root",password="livewire",database="festival")
some=add.cursor()
#some.execute("create table diwali(dressn varchar(50),crackerbox int,food varchar(50))")
some.execute("insert into diwali(dressn,crackerbox,food)values('kutriset',3,'vegmeals')")
some.execute("select * from diwali")
details=some.fetchall()
print(details)
add.commit()



  
