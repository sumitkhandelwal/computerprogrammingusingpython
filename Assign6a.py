#Assignment no: 6(A)
#Select a text file and count number of words, Lines, Characters.
num_chars = 0   # Assign Value 0 for all variable
num_words = 0
num_lines = 0

# Using Promt create a file in write mode and insert data
# Ex :
# >>> f = open("d:\sample.txt","w")
# >>> f.write('I am from Pune\n I like Python\nI am in MITAOE')
# >>> f.close()

# Open file in read  mode
f = open("d:\sample.txt","r")
#Consider each line for counting the words and chars.
for line in f:     # for loop is rotate as per file object
    word = line.split()  # Seperate the word from line.
    num_words += len(word)  # update the count value of words
    num_lines += 1  # # update the count value of lines
    num_chars = len(line) # update the count value of characters
print num_chars  # print all values.
print num_words 
print num_lines
