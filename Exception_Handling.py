
# Three types of error can be generated in this code
# 1. Input should be int but user enters string/char
# 2. a/b division can't be performed if divided by zero
# 3. Some other Unexpected Error

try:
    print("Resource Opened...")
    print("a / b will be performed")
    a = int(input("Enter value number a : "))
    b = int(input("Enter value number b : "))

    result = a/b

    print("Ans (a/b) --> {}".format(result))

except ValueError as e:
    print("ValueError Caught --> ", e)

except ZeroDivisionError as e:
    print("ZeroDivisionError Caught --> ", e)

except Exception as e:
    print("Exception --> {}", e)

finally:
    print("Resource Closed...")

