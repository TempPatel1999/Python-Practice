
# Sorted array is give
# Apply binary search to search an element in an array (sorted)

pos = -1
num_of_iteration = 0

def search(list, n):

    length = len(list)
    lower_bound = 0
    upper_bound = length

    while lower_bound <= upper_bound:
        globals()["num_of_iteration"] += 1
        mid_index = ( lower_bound + upper_bound ) // 2        # "//" is used to divide a number and get an integer as output
        mid_value = list[mid_index]
        if mid_value == n:
            globals()["pos"] = mid_index
            return True
        else:
            if n > mid_value:
                lower_bound = mid_index + 1
            else:
                upper_bound = mid_index - 1
    return False


# Sorted List
list = [4,5,23,25,65,88,99]

n = 0

if search(list, n):
    print("Element found at {}...".format(pos+1))
else:
    print("Element not found")

print("Number of iteration = {}".format(num_of_iteration))