# Assignment No: 5(C)
# Choose cricket team of eleven players find the captain
# of the team (consider tallest person as a captain).
# Form a cricket team with Eleven player
cricket = list(input("Enter the player's Height :"))
print "No of players in team", len(cricket)
print "Height of Player", cricket 
# consider first player height is maximum height 
maximum = cricket[0]
# Trace the team with reference to height 
for i in range(1, len(cricket)):
    if cricket[i] > maximum : #other player are taller than previous one 
        maximum = cricket[i]  # Update the value of height
# Print the height which is maximum and declear he is caption
print "Selected caption of my team with Height is :", maximum 


