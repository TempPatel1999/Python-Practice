
# Fibonacci function using generator


def fibo(limit):

    a, b = 0, 1
    i = 0
    while i < limit:
        yield a         # Generator
        a, b = b, a+b
        i += 1


# Take input number
num = int(input("Enter how many first fibonacci number do you want : "))

# Function called
result = fibo(num)

# Output Printed
for i in range(num):
    print("{} --> {}".format(i+1, result.__next__()))
    # Or print(next(result))
