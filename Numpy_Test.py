import numpy

#Creating arrays in 6 ways using numpy
#1. array()
#2. linspace()
#3. logspace()
#4. arange()
#5. zeros()
#6. ones()

array1 = numpy.array([1,2,3])
print("array 1 :", array1)

print("********************************************")

array2 = numpy.linspace(1,15,3)
print("array 2 :", array2)

print("********************************************")

array3 = numpy.logspace(1,15,3)
print("array 3 :", array3)
print('%.2f' %array3[1])

print("********************************************")

array4 = numpy.zeros(5)
print("array 4 :", array4)

print("********************************************")

array5 = numpy.ones(5,int)
print("array 5 :", array5)

#Coping Array

original_Array = numpy.array([10,20,30,40,50])
copied_Array = original_Array.copy()

print("Original array :",original_Array," Address :",id(original_Array))
print("Copied array :",copied_Array,"Address :",id(copied_Array))


#Addition of arrays using loop

a1 = numpy.array([1,2,3,4,5])
a2 = numpy.array([5,4,3,2,1])
sum = numpy.zeros(5)

for i in range(5):
    sum[i] = a1[i]+a2[i]


print("Addition of two arrays")
print(a1)
print(a2)
print(sum)

#Maximum of an array (a1 here)

print("Max in array")

for i in range(len(a1)):
    if i==0:
        max = a1[0]
    elif a1[i]>=max:
        max = a1[i]

print("a1 :",a1)
print("Max:", max)