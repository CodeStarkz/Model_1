# advanced_python_work.py

"""
Classes are like bundle that helps us to put the like thing togeather
inside the classes functions are known as methods and variables are known as atributes

multi threading and multi processing

multi threading is a way to execute multiple tasks at the same time - paralell processing



"""

import threading
import time
num_holder=[]
letter_holder=[]
def print_numbers():
    for i in range(1,11):
        num_holder.append(i)
        print(i)

        time.sleep(1)
    print(num_holder)


def print_letters():
    for i in "Python":
        letter_holder.append(i)
        print(i)
        time.sleep(1)
    print(letter_holder)



# creating threads
if __name__ == "__main__":
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)

# thread start
    t1.start()
    t2.start()



    t1.join()
    t2.join()

    print("Process ended successfully")

    print(num_holder + letter_holder)







