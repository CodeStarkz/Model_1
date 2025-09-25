import time
import threading
# Case Study 1
time1=time.perf_counter() # start measuring time

def even_no_extractor(X): # operation 1
    even=[]
    for i in range(X):
        if i %2 ==0:
           even.append(i)
        else:
            pass
    return(even)

def continious_sum(X):   #Operation 2
    total_sum=0
    for i in range(X):
        total_sum+=i
    return total_sum


print(continious_sum(50))
print(even_no_extractor(50))

time2=time.perf_counter()

print(time1)
print(time2)
print(time2-time1)


#Case Study 2 (with Multithreading)
t3=time.perf_counter()
instance1=threading.Thread(target=even_no_extractor(50))
instance2=threading.Thread(target=continious_sum(100))
t4=time.perf_counter()

print(f"timetaken={t4}-{t3}", t4-t3)