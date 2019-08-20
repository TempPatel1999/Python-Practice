import array

array_Object = array.array('i',[])


#Creating array
size_Of_Array = int(input("Enter size of array : "))

for i in range(size_Of_Array):
    x = int(input("Enter Value : "))
    array_Object.append(x)

print("Array Created : ",array_Object)


#Reversing the array without using in-built function

mid = int(size_Of_Array/2)
i = 0
j = size_Of_Array-1

while i < mid:
    array_Object[i],array_Object[j] = array_Object[j],array_Object[i]
    j-=1
    i+=1

#Print Reverse array
print("Reverse array : ",array_Object)



#Delete Value on a given Index
index = int(input("Enter index to be deleted : "))

for i in range(index,len(array_Object)-1):
    array_Object[i]=array_Object[i+1]

array_Object[len(array_Object)-1] = 0

#Print Deleted array
print("After deleting : ",array_Object)
