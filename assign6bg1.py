#Assignment No 6(B)
#Choose the words from the file, store in the list and
#sort the list is ascending order.
# Create a a new file in write mode and insert random data and close it
f = open("e:\sample123.txt",'w')
f.write('abc \n pqr \n abcc \n abb \n xyz \n dfr')
f.close()
#create a empty list 
a1 = [ ]
#open same file in read mode and trace all lines
f = open("e:\sample123.txt",'r')
for line in f: 
    line = line.strip() #we remove the white space in each line
    a1.append(line) # add each line in a list in append mode
    a1.sort() # sort in ascending order 
print a1 #print list item/elements
f.close() # Close the file.
