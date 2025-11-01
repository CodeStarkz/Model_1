# # creating program for prime number detection
# n= int(input("enter your number:"))
# for i in range(2,n):
#     if n%i==0:
#         print(f"{n} is a prime number")
#         break
#     else:
#         print(f"{n} is not a prime number")
"""
To generate prime numbers10

"""
from prometheus_client.validation import enable_legacy_validation

"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_nth_prime(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
            print(num)
            if count == n:
                return num
        num += 1
    return num


n = int(input("Enter n to find nth prime number: "))
result = find_nth_prime(n)
print(f"The {n}th prime number is: {result}")


# Number gusser """
import random

# n=random.randint(1,10)
# print(n)
#
# while True:
#     print(n)
#     try:
#         x=int(input("enter the next number:"))
#         if x!= n:
#             print("entered number is not same as previous")
#             print(x)
#         else:
#             print("entered number is same as previous")
#
#     except ValueError:
#         print("bla_bla")

# fibonacchi

#
# def Fibonacchi(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return Fibonacchi(n-1)+Fibonacchi(n-2)
#
# Fibonacchi(10)


# def fibo(n):
#     a,b=0,1
#     for i in range(n):
#         a,b=b,a+b
#         print(a,end=" ")
#
# fibo(15)


def fibonacci3(n):
    elements = {1:1, 2:1}
    def inner(n):
        if n not in elements:
            next_element = inner(n-1) + inner(n-2)
            elements[n] = next_element
        return elements[n]
    return inner(n)


fibonacci3(20)