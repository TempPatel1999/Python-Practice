# Selection Sort: Minimum is selected among the array and swapped on the front
# after swapping front is incremented


def search(list):

    for i in range(len(list)-1):
        min_index = i
        for j in range(i, len(list)):
            if list[j] < list[min_index]:
                min_index = j               # Find minimum index

        list[min_index], list[i] = list[i], list[min_index]         # Swap and bring min at front
        print(list)


# Main Program
nums = [6, 5, 4, 3, 2, 1]
print(nums)
search(nums)
