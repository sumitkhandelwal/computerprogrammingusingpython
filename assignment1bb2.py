# To find mile_per_gallon values

# Take the value of distance and gas utlization.
kilometer = float(input("Enter the value of distance in Kilometer : "))
gallon = float(input("Gas Utilized by an object to cover distance : "))

# Convert distance in miles
miles = 0.6321 * kilometer

# To find mile_per_gallon value
mile_per_gallon = (miles / gallon)

#print the result
print "Calculated value of Mile_Per_Gallon :",mile_per_gallon

#Output:

#Enter the value of distance in Kilometer: 45
#Gas Utilized by an object to cover distance : 3.56
#Calculated value of Mile_Per_Gallon : 7.99002808989
