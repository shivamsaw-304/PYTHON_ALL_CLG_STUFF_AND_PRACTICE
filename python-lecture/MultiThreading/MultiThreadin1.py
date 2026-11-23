import threading 
from threading import Thread

openfile = open("threading.txt" ,"w")
op

def task():
    for i in range(100):
        print(i)


thread1 = Thread(target=task)

thread1.start()
