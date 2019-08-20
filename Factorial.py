import math

input_Number = int(input("Enter number : "))

#Math Function
factorial1_Answer = math.factorial(input_Number)

#Manual Calculation

factorial2_Answer = 1
for i in range(input_Number,0,-1):
    factorial2_Answer = factorial2_Answer * i


print("Using math function Factorial =", factorial1_Answer)

print("Using manual method Factorial =", factorial2_Answer)