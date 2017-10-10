#Assignment No 5(c)
#Choose cricket team of eleven players
#find the captain of the team (consider tallest person as a
#captain)

a = [3.5,6.7,3.8,4.6,5.1,6.6,7.0,4.9,4.2,5.9,6.0]
print "Heights of all eleven player as follows: \n",a
maximum = a[0]
for i in range(1,len(a)):
    if a[i] > maximum:
        maximum = a[i]
print "Height of My team caption is :", maximum
