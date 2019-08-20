import functools

#Any Random numbers in a list
num = [0,1,2,3,4,5,6,7,8,9]

#Filter : even numbers to be filtered out from num list
evens = list(filter(lambda a: a%2==0,num))

print(evens)

#Map : Make changes/Map in each value of list items (Here double each value of even list)
double = list(map(lambda a:a*2 ,evens))

print(double)

#Reduce : Combine/Reduce all value of list into one (Here sum of double list is made)
sum = functools.reduce(lambda a,b:a+b,double)

print(sum)