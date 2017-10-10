#Assignment No : 6 (C)
#Create duplicate the file from an original file.
# Take file contents from user
str1 = raw_input("Enter the contents in file")
# Create a new file in write mode
ori = open("E:\original.txt",'w')
ori.write(str1) # Insert the contents in file
ori.close() # close the file
# reopen original file in read mode and create duplicate file write mode
ori = open("E:\original.txt",'r')
dup = open("E:\dublicate.txt",'w')
#trace the line in original file
for line in ori.read():
    dup.write(line) # update in duplicate file
# close the file for security
ori.close()
dup.close()
# open duplicate file for checking updatation in read mode
dup = open("E:\dublicate.txt",'r')
print "Data inserted in duplicate file :",dup.read() # Check the contents.
