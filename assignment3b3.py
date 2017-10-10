# Show the distance in miles per gallon with
# respect user defined value in Python

# Take values of distance in Kilometer and gas utilization in gallon 
km = float(input("Take the distance value in kilometer : "))
gallon = float(input("Enter gas utlization to cover given distance : "))
#calculate distace value in miles from distance value in kilometer
miles = km * 0.6321
#Calculate Mile_per_gallon from input values
mile_per_gallon = miles/gallon
#print the result.
print "Miles per Gallon with repsect to distance is : ",mile_per_gallon
