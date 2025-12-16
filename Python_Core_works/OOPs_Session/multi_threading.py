"""import time
import threading


t1=time.time()
def sq(n):
    skr=[]
    for i in range(n):
        time.sleep(1)
        skr.append(i**2)

    print(skr)

def cb(n):
    cbr=[]
    for i in range(n):
        time.sleep(1)
        cbr.append(i**3)
    print(cbr)

t1=time.time()

task1=threading.Thread(target=sq,args=(10,))
task2=threading.Thread(target=cb,args=(10,))
task1.start()
task2.start()
task1.join()
task2.join()



t2=time.time()
print(t2-t1)



"""


import time
import threading
import multiprocessing
sqrlist=[]
cblist=[]

def sqr(n):
    for i in range(n):
        time.sleep(.1)
        sqrlist.append(i**2)
    print(sqrlist)

def cb(n):
    for i in range(n):
        time.sleep(.1)
        cblist.append(i**3)
    print(cblist)

def main():
    t1=time.time()
    task1=threading.Thread(target=sqr,args=(10,))
    task2=threading.Thread(target=cb,args=(10,))

    task1.start()
    task2.start()
    task1.join()
    task2.join()
    t2=time.time()
    print(t2-t1)

if __name__=="__main__":
    main()
