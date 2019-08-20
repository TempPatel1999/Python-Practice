
# Search method has a functionality to search for element in a particular list


pos = -1

# Definition Declaration
def search(list, n):

    length = len(list)

    for i in range(length):
        if list[i] == n:
            globals()["pos"] = i
            return True

    return False

# Main Program Execution
list = [5,3,9,7,1,6,2]

n = int(input("Enter element to be searched: "))

if search(list, n):
    print("Element found at {}...".format(pos+1))
else:
    print("Element not found...")