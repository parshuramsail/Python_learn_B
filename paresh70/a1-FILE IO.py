#FILE IO-BASICS
f=open("sail.text","rt")
contend=f.read(4)
print(contend)
f.close()

#
#print new line after new sentence(print sentences one line after another line)
f=open("sail.text","rt")
#contend=f.read()
for line in f:
    print(line)

f.close()

#
f=open("sail.text","rt")
contend=f.read()
for line in contend:
    print(line)

f.close()

#FILE IO-BASICS
f=open("sail.text","rt")
contend=f.read(3333)
print(contend)
contend=f.read(3333) # line is not execute ( upeer line only executed) blank content (for more information see below program
print(contend)  # not executr
f.close()

#print only one line
f=open("sail.text","rt")
print(f.readline()) #print only one line
f.close()

# READLINE=how much time you use this command that much time it print the lines
f=open("sail.text","rt")
print(f.readline()) #print only one line
print(f.readline()) #print another line
f.close()

# to store lines in list buy using (f.readlines)
# to store lines in list buy using (f.readlines)
#print only one line
f=open("sail.text","rt")
print(f.readlines())
f.close()
