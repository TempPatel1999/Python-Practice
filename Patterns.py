num = int(input("Enter Number:"))


#####################################################################################

print("\n\nPattern 1")

for i in range(num):
    for j in range(num):
        if i>=j:
            print(chr(65+j) ,end="")
        else:
            print(chr(65+14+j),end="")
    print()



#####################################################################################


print("\n\nPattern 2")


for i in range(num):
    temp = i
    for j in range(num-i):
        temp = temp+1
        print(temp,end="")

    print()
