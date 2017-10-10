# To predict weather given number is even or odd

# Take any number
n = int(input("Enter any number to check weather it is even/odd : "))

# Condition, if no is divisible by 2 exactly then even otherwise odd
if(n % 2 == 0) :
    print "Given number : ",n," is even number"
else:
    print "Given number : ",n," is odd number"

