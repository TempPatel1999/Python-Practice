num = int(input("Enter number to be checked prime or not : "))


###################################### for else method ########################################


for i in range(2,int(num/2)):
    if num%i == 0:
        print("**Not Prime")
        break
else:
    print("**Prime")



###################################### Normal Method ##########################################


NotPrime_flag = 0

if(num<2):
    print("Not Prime")
    exit()

for i in range (3,int(num/2)):
    if(num%i==0):
        NotPrime_flag = 1
        break

if(NotPrime_flag == 0):
    print("Number is Prime")
else:
    print("Number is not Prime")
