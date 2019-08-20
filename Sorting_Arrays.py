
import array

array_Object1 = array.array('i',[30,60,10,20,50])

#Unsorted
print("Unsorted Array 1")
for i in array_Object1:
    print(i)



print("***************************************")


#Sorting Logic

for i in range(len(array_Object1)-1):
    for j in range(i+1,len(array_Object1)):
        if(array_Object1[i]>array_Object1[j]):
            array_Object1[i],array_Object1[j] = array_Object1[j],array_Object1[i];  #Swapping Logic


#Sorted

print("Sorted Array 1")
for i in array_Object1:
    print(i)

