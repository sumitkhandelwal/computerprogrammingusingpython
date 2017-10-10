#Find the kinetic energy of an object.

# Take value of mass and velocity of moving object
mass = float(input("Enter the mass value of an object : "))
velocity = float(input("Enter the velocity of an object :"))
# Calculate the kinetic energy of an object
KE = (0.5 * mass * (velocity ** 2))

# print
print "The kinetic energy of an object is  :",KE,"Joule"

#Output
#Enter the mass value of an object : 34.56
#Enter the velocity of an object :54.6
#The kinetic energy of an object is  : 51514.4448 Joule
