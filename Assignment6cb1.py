# Assignment No 6(C)
# Create duplicate the file from an original file.
file1 = raw_input("Enter the name of source file with address :")
data = raw_input("Insert data in a file :")
file2 = raw_input("Enter the name of destination file with address :")
s = open(file1,'w') # Create a file and insert data in a file
s.write(data)
s.close() # close file for security reason
s = open(file1,'r') # Open source file read mode 
d = open(file2,'w') # Open Destination file in write mode
for line in s.read(): # COpy and Paste line by line 
    d.write(line)
s.close()
d.close()
s = open(file1,'r') # Open files in read mode and check the contents 
d = open(file2,'r')
print "Data in source file is :",s.read()
print "Data in destination file is :",d.read()
s.close()
d.close()
