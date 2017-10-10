# To find the reverse of given number
n = input("Enter any 5 digit number :") # To take the data from User
rev = 0 # rev is worked as a input and output
a = n % 10 # n = 12345, a = 12345 % 10, a = 5
n = n/10    #n = 12345 , n = 12345 / 10 , n = 1234
rev = rev + a * 10000 # rev =0, rev = 0 + 5 * 10000, rev = 50000
a = n % 10 # n = 1234, a = 1234 % 10, a = 4
n = n/10    #n = 1234 , n = 1234 / 10 , n = 123
rev = rev + a * 1000 # rev =50000, rev = 50000 + 4 * 1000, rev = 54000
a = n % 10 # n = 123, a = 123 % 10, a = 3
n = n/10    #n = 123 , n = 123 / 10 , n = 12
rev = rev + a * 100 # rev =54000, rev = 54000 + 3 * 100, rev = 54300
a = n % 10 # n = 12, a = 12 % 10, a = 2
n = n/10    #n = 12 , n = 12 / 10 , n = 1
rev = rev + a * 10 # rev =54300, rev = 54300 + 2 * 10, rev = 54320
a = n % 10 # n = 1, a = 1 % 10, a = 1
n = n/10    #n = 1, n = 1 / 10 , n = 0
rev = rev + a * 1 # rev =54320, rev = 54320 + 1 , rev = 54321

print "Resevese of Given Number is :",rev
