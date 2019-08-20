
# Apply bubble sort on a list of integers
# Bubble sort : This algorithm works by repeatedly swapping the adjacent elements if they are in wrong order.


def sort(list):

    for i in range (len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1],list[j]      # Swap


nums = [4, 2, 5, 7, 1, 3, 8, -1, 0]

sort(nums)
print(nums)