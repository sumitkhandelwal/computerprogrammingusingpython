#Assignment No 6(A)
#Select a text file and count number of words, repeated words in a file.
#Create a file in write mode and update the data in a file and close it
file1 = raw_input("Enter file name with address and extension : ")
data = 'ABC \n PRQ \n XYZ \n  ABC \n ABC \n PQR \n XYZ \n GHI'
f = open(file1,'w')
f.write(data)
f.close()
# Reopen same file in read mode and perfrom an operation and close it.
f = open(file1,'r')
count = 0   #declear a counter to count no of words in file
a1 =[]         # Here we take empty list to hold all words
for line in f:   # for loop for travelling an array using file
    line  = line.strip()  #To remove white space character in word or file
    a1.append(line)   # Add word in list one after another
    count = count + 1 # Update counter with each opeartion
print "The words in file is : ", a1  # Print the list
print "Total Number of Words in file is :", count # print the counter value
f.close() # close the file
dic = {}  # Create empty dictionary hold the count value and word(ID)
for x in a1:  # Trace each word in a list using loop 
    if not x in dic:  # check the word is not present in list, update its count value. 
        dic[x]= a1.count(x)  # Update only count value for duplicate word.
print "Count of Each word in File : ",dic  # Print the Repeated word using Dictionary
