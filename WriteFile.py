file = open("test.txt")

# print all contents of file
#print(file.read())

#read 6 bytes contents of file
#print(file.read(6))


# readline reads the file line by line at a time
# line = file.readline()
 #while line!="":
  #  print(line)
  #  line = file.readline()

#Amother way to print file line by line
for line in file.readlines():
    print(line)
file.close()
