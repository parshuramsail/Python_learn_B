# WRITE FILE
#f=open("ram1.txt","w")
#f.write("code with harry")
#f.close()

# APPEND
#f=open("ram1.txt","a")
#f.write("code with harry \n")
#f.close()

# READ AND WRITE MODE
f=open("ram.txt","r+")
print(f.read())
f.write(" THANK YOU")
f.close()
