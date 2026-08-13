'''import threading, time
t=threading.Lock()
def win(Name):
    for x in range(2):
        print(f"{Name},range{x}")
        time.sleep(2)
t1=threading.Thread(target=win,args=("swetha",))
t2=threading.Thread(target=win,args=("monika",))
t1.start()
t2.start()
t1.join()
t2.join()
def app(name):
    for i in range(3):
        print(f"{name},mark{i}")
        time.sleep(2)
t3=threading.Thread(target=app, args=("ravi",))
t4=threading.Thread(target=app,args=("mohan",))
t5=threading.Thread(target=app,args=("banu",))
t3.start()
t4.start()
t3.join()
t4.join()
t5.start()
t5.join()'''

'''import threading ,time
t=threading.Lock()
def win(name):
    for i in range(1):
      print(f"{name},mark{i}")
    time.sleep(2)
t1=threading.Thread(target=win,args=("swetha",))
t2=threading.Thread(target=win,args=("priyanka",))
t2.start()
t2.join()
t1.start()
t1.join()
def app(name):
    for x in range(2):
        print(f"{name},digit{x}")
    time.sleep(1)
t3=threading.Thread(target=app,args=("sowndariya",))
t3.start()
t3.join() 
def some(name):
    for y in range(3):
        print(f"{name},mark{y}")
    time.sleep(3)
t4=threading.Thread(target=some,args=("sangari",))
t4.start()
t4.join()'''
import threading,time
t=threading.Lock()
def app(name):
    for i in range(3):
        print(f"{name},regno{i}")
    time.sleep(3)
t1=threading.Thread(target=app,args=("jayanthi",))
t2=threading.Thread(target=app,args=("nisha",))
t1.start()
t1.join()
t2.start()
t2.join()



