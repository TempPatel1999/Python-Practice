import math

def fib(n):

    a = 0
    b = 1

    if n <= 0:

        print("Invalid")

    elif n == 1:
        print(a)

    else:

        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)


def modFibo(n):
    a = 0
    b = 1
    c = 1

    if n <= 0:

        print("Invalid")

    elif n == 1:
        print(a)

    else:

        while c < n:
            c = a + b
            a = b
            b = c

        print(a)


#Zzzzzzzzzz
num = int(input("Enter number : "))
print("*********************Mod Finonacci Series*****************************")
modFibo(num)
print("**********************Finonacci Series********************************")
fib(num)
