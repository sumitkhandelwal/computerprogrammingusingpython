#Assignment No :6(B)
# Take the words from file and arrange it in sorted form.
# Take the file and insert data in a file and close it
file1 = raw_input("Enter the name of file with address:")
data = "ABC\nPQR\nXYZ\nABD\nAAA\nGEF\nWXY"

f = open(file1,'w')
f.write(data)
f.close()

a = [] # Take empty list/array for holding the words
f = open(file1,'r') # open a file in read mode.
for line in f: # Take the data line by line from a file
    line = line.split() # Seperate words from each line.
    a.append(line) # Add seperated word into in an array.
print "Words present in a file: \n",a # print array.
f.close() # close the file for security.
# Use Bubble sort algorithm.
print ("1. For Ascending order \n2. For Descending Order ")
choice = int(input("Enter your choice :"))
if(choice == 1):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print "Words present in Sorted form :\n",a
if(choice == 2):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if(a[j] < a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
print "Words present in Sorted form :\n",a

