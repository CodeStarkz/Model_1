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

