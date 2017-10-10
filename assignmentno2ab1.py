# The find the result of student
    #  Take the mark values from users (subject count = 5)
    print "\n $$$Enter",i+1,"Student's Details $$$ "
    m1 = int(input("Enter the mark of first subject :"))
    m2 = int(input("Enter the mark of second subject :"))
    m3 = int(input("Enter the mark of third subject :"))
    m4 = int(input("Enter the mark of fouth subject :"))
    m5 = int(input("Enter the mark of fifth subject : "))

    # Calculate the total mark obtained
    sum1 = m1 + m2 + m3 + m4 + m5

    # Percentage of marks
    per =(float(sum1)/500) * 100

    #print the result
    print "Total Marks obtained in Exam : ",sum1,"/500"
    print "Percentage of Student is :",per,"%"

    # Calculate a grade
    if(per < 50) :
        print("Student's result is : Fail")
    elif(per >= 50 and per < 60) :
        print("Student's result is : Second Class")
    elif(per >= 60 and per < 75) :
        print("Student's result is : First Class")
    else:
       print("Student's result is :First Distinction")

    # Subject wise result.
    if (m1 < 49):
        print "Student is fail in subejct - m1"
    if (m2 < 49):
        print "Student is fail in subejct - m2"
    if (m3 < 49):
        print "Student is fail in subejct - m3"
    if (m4 < 49):
        print "Student is fail in subejct - m4"
    if (m5 < 49):
        print "Student is fail in subejct - m5"
        
# Output
#Enter the mark of first subject :56
#Enter the mark of second subject :45
#Enter the mark of third subject :67
#Enter the mark of fouth subject :54
#Enter the mark of fifth subject : 35
#Total Marks obtained in Exam :  257 /500
#Percentage of Student is : 51.4 %
#Student's result is : Second Class
#Student is fail in subejct - m2
#Student is fail in subejct - m5
