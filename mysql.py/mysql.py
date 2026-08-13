import pymysql as sql;
database= sql.connect(host="localhost",user="root",password="livewire")
cursorobj=database.cursor()
cursorobj.execute("create database stuinfo")
link=sql.connect(host="localhost",user="root",password="livewire",database="stuinfo")
curser=link.cursor()
curser.execute("select * from student")
details=curser.fetchall()

