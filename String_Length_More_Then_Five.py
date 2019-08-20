
#Funtion Definition
def compute(num_of_input):

    lst = []

    #Take 5 names from user
    for i in range(num_of_input):
        name = input("Enter name:")
        lst.append(name)

    print("***************************************************")

    #Program Logic
    word_count = 0

    for i in lst:
        letter_count = 0
        for j in i:
            letter_count += 1

        if letter_count>5:
            word_count += 1

    return word_count


#Zzzzzzzzzzzzzzzzz
num_of_input = int(input("Enter num of Input:"))

#Function Called
word_count = compute(num_of_input)

# Print Output in a new way
print("Num of Words greater than 5 letters for {} words are.... {} ".format(num_of_input, word_count))
