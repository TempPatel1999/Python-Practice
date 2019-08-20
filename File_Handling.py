# file_reference_name = open("File_Name","Mode")
# Mode
# r  --> Read
# w  --> Write
# a  --> Append
# rb --> Read binary (Can be used to read image type files)
# wb --> Write binary (Can used to write image type files)

#################### Write a file ####################

print("Writing Started...")

f = open("File", "w")        # To create file or to write (actually override) on existing file

f.write("Hy Z...")
f.write("\nYou are the best...")
f.write("\nHope to see you soon...")

f.close()                   # This will save the file

print("Writing Done....")

#################### Read a file ####################

print("Reading Started...")

f1 = open("File", "r")

print(f1.readline(), end="")
print(f1.readline(), end="")
print(f1.readline(), end="")

# OR

# for i in f1:
#    print("i", i)

f1.close()

print("\nReading Done...")

#################### Append a file ####################

print("Appending Started...")

f2 = open("File","a")

f2.write("\n143")

f2.close()

f2 = open("File","r")
for i in f2:
    print(i, end="")
f2.close()

print("\nAppending Done...")

