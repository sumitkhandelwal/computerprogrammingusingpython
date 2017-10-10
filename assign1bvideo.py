
#Show the distance in miles per gallon with respect user defined value in Python.

#input

km = float(input("Enter the distance in KM: "))
gallon = float(input("Enter the gas utilization in gallon :"))

#calculation

miles = km * 0.621
mile_per_gallon = (miles/gallon)

#print of result

print "Miles per Gallon of Given data is :",mile_per_gallon
