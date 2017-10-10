# Assignment No : 6(A)
# Select the file, count number of words and repeated word
# Create a file and insert data into the file
file1 = raw_input("Enter the file name with folder address :")
data = 'ABC\nCDR\nEFG\nABC\nXYZ\nXYZ\nPQR\nCDR'
f = open(file1,'w')
f.write(data)
f.close() # We close the file for security.
a = [] # Define Array/List to hold the file data for operation.
f = open(file1,'r') # Open file in read mode.
for line in f: # Check each line in file
    line = line.split() # seperate each word with respect to space or newline
    a.append(line) # insert the data in list/array from last location.
    #a.sort()
print a # print the array
dict3 = {} # Create a dict.
for x in a:  # Trace each and every element in list 
    if not x in dict3:   # Element found in list or not 
        dict3[x] = a.count(x)  # if found the update the count and value also
print dict3       # print dict
