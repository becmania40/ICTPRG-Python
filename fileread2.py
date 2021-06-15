# Read a text file and print it.
#  Automatically opened in read mode 'r'
file1 = open("day02.txt")
lines = file1.readlines()
for line in lines:
    print(line)
file1.close()