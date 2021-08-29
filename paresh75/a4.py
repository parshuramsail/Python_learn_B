# to know the file pointer location
#f=open("ram.txt")
#print(f.tell())
#print(f.readline())
#print(f.tell())
#print(f.readline())
#f.close()

# FILE POINTER RESET
#f=open("ram.txt")
#print(f.readline())
#f.seek(0)
#print(f.readline())
#f.close()


# DONT NEED TO CLOSE FILE WHEN USING BELOW LINE
with open("ram.txt") as f:

