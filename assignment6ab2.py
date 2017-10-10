# Assignment 6(A) Create duplicate file from any source file.
# Take the label of Source file and Destination file with address Location
file1 = raw_input("Enter the source file name with address :")
data = raw_input("Enter the data from file :") # Take Source file data.
file2 = raw_input("Enter Duplicate file name with address:")
f = open(file1,'w') # Open file in write mode (i.e. New file creation)
f.write(data) # Insert the data into file.
f.close() # Close the file for security purpose. 
f = open(file1,'r') # Open source file in read mode for fetching 
d = open(file2,'w') # Open destination file for insert the content in file.
# Line by line data is going to tranfer from one file to another.
for mit in f.read():  # Take a loop with one variable and hold complete line 
    d.write(mit)# in a variable and perfrom write operation using write 
# function with a variable.
f.close()  # Close the file for security purpose. 
d.close() # Close the file for security purpose. 
# To display the contents in both file, for that we open both file in 'r' mode.
f = open(file1,'r') 
d = open(file2,'r')
print "Source file data : ", f.read()#Display the content using print statement
print "Destination file data :",d.read()
f.close()# Close the file for security purpose. 
d.close() # Close the file for security purpose. 

