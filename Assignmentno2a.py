#Write a Python program for printing result of five subjects for student.
n = int(input("Enter the count of Student :"))
for i in range(1,n+1):
    print "Enter the marks details of student :",i
    # Take the make of 5 subject
    m1 = int(input("Enter the mark of first subject: "))
    m2 = int(input("Enter the mark of second subject: "))
    m3 = int(input("Enter the mark of third subject: "))
    m4 = int(input("Enter the mark of fourth subject: "))
    m5 = int(input("Enter the mark of fifth subject: "))
    # Addition of obtained marks.
    sum1 = (m1+m2+m3+m4+m5)
    # Calcuate Average Mark
    avg = (float (sum1)/5)
    #Calculate Percentage
    per = (float (sum1)/500) * 100
    print "Total Marks obtained :",sum1
    print "Average Marks obtained :",avg
    print "Percentage of Student :",per
    # Calculate Grade
    if(per > 95):
        print " Grade A"
    elif (per > 85 and per <=95):
        print "Grade B"
    elif (per > 80 and per <=85):
        print "Grade C"
    elif (per > 75 and per <=80):
        print "Grade D"
    elif (per > 70 and per <=75):
        print "Grade E"
    else:
        print "Grade F"
    # Subwise passing
    if(m1 < 60):
        print "You are fail in subject : m1"
    if(m2 < 60):
        print "You are fail in subject : m2"
    if(m3 < 60):
        print "You are fail in subject : m3"
    if(m4 < 60):
        print "You are fail in subject : m4"
    if(m5 < 60):
        print "You are fail in subject : m5"

#output

#Enter the mark of first subject: 45
#Enter the mark of second subject: 56
#Enter the mark of third subject: 67
#Enter the mark of fourth subject: 5
#Enter the mark of fifth subject: 47
#Total Marks obtained : 220
#Average Marks obtained : 44.0
#Percentage of Student : 44.0
#Grade F
