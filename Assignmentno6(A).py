# Assignment No 6(B)
# Choose the words from the file, store in the list and
#sort the list is ascending order..
file1 = raw_input("Enter the name of source file with address :")
data = 'abc\npqr\nxyz\nsad\nyzq'
f = open(file1,'w') # Create a file and insert data in a file
f.write(data)
f.close() # close file for security reason
f = open(file1,'r') # Open source file read mode
a = []  # declare empty list
for line in f: # trace the lines from files
    line = line.split() # seperate the words as per white space characters
    a.append(line) # Add the data in list at last
print "Data in file is :\n",a # print the list
# Use Bubble sort for sorting purpose.
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print "Data is in sorted form :\n",a
