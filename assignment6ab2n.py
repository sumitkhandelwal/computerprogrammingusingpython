# Assignment No : 6(A)
# Program to Count Number of Lines, Words and Characters in file.
# Create a new file and insert a data in a file
file1 = raw_input("Enter the name of file with address:")
data = "ABC PQR\nsadas"
f = open(file1,'w') 
f.write(data)
f.close()
# open file in read mode and fetch the data line by line
f = open(file1,'r')
count = 0 # for line count 
char = 0 # for Character count
nword = 0 # for word count
for line in f: # Fetch line by line data from file
    words = line.split() # Count no of word in each line and split it
    count = count + 1 # Count no of line in file
    char = char + len(line) # Count no of characters in file
    nword = nword + len(words) # Count no of Words in file
print "Total No of line in my file is :", count # print line count
print "Total No of characters in my file is :", char # print character count
print "Total No of words in my file is :", nword # print word count
f.close()
