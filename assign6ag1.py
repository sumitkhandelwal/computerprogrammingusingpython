#Assignment No 6(B) and 6(A)
# Select a text file and count number of words, repeated words in a file.
# Create  new file in write mode and enter some contents inside the file and close it
file1 = raw_input("Enter a file name with an address and extension")
f = open(file1,'w')
f.write('abc \n prq \n xyz \n abc \n pqr \n abc')
f.close()
# Declear a list(infinite)
a1 = []
#open same file in read mode to perfrom a defined operation.
f = open(file1,'r')
# Line by line fetch the data from file and store in a variable.
num_words = 0
for line in f: 
    line = line.strip() # To remove white space using strip() method
    word = line.split() # To seperate each and every word in file
    a1.append(line) # Append (insert) the line at the end of line in a list
    num_words += len(word)  
print a1# Print the list
print "Number of words in List is :", num_words

dic = {}  # create a empty dictionary 
for x in a1: # Check each word in list 
    if not x in dic:  # Check it is in dictionary,if present add it and update the count 
        dic[x] = a1.count(x)  # Update the count of word in dict
print dic  # print Dictionary 
        
