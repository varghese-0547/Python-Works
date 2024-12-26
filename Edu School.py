print("Welcome to EDU Public School")
print ("How can we help you...")
print("1 = Admission\n2 = Login")
ch=int(input("Please enter your choice :"))
if ch==1:
    print("Select the class",1,2,3,4,5,6,7,8,9,10,11,12)
    class1= int(input("Enter the class : "))
    if class1<=10:
        name = input("Enter student name :")
        dob = input("Enter your Date of Birth :")
        fn = input ("Enter father's name :")
        ph = int(input("Enter father's phone number :"))
        mn = input("Enter mother's name :")
        ph = int(input("Enter mother's phone number :"))
        pin = int(input("Enter your pin code :"))
        ads = input("Enter your adress :")
        ri = input ("Enter your Caste :")
        cht=input("Do you want transportation facility from the school :")
        if cht==("Yes"):
             bdp1=input('Enter your boarding point :')
             print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

             print("# School timing is from 08:30 am to 03:00 pm")
             print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
        elif cht==("yes"):
             bdp1=input('Enter your boarding point :')
             print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

             print("# School timing is from 08:30 am to 03:00 pm")
             print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
        elif cht==("YES"):
             bdp1=input('Enter your boarding point :')
             print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

             print("# School timing is from 08:30 am to 03:00 pm")
             print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
        else :
            print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

            print("# School timing is from 08:30 am to 03:00 pm")
            print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
    if class1>10 and class1<=12:
        print("Enter your stream:\n1 = Science\n2 = Commerce\n3 = Humanities\n")
        b=int(input("Enter your stream:"))
        if b==(1):
            print("Select your batch\n1 = Bio Maths\n2 = Computer Science\n3 = Bio Info")
            input("Enter your batch :")
        name = input("Enter student name :")
        dob = input("Enter your Date of Birth :")
        fn = input ("Enter father's name :")
        ph = int(input("Enter father's phone number :"))
        mn = input("Enter mother's name :")
        ph = int(input("Enter mother's phone number :"))
        pin = int(input("Enter your pin code :"))
        ads = input("Enter your adress :")
        ri = input ("Enter your Caste :")
        cht=input("Do you want transportation facility from the school :")
        if cht==("Yes"):
             bdp1=input('Enter your boarding point :')
             print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

             print("# School timing is from 08:30 am to 03:00 pm")
             print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
        elif cht==("yes"):
             bdp1=input('Enter your boarding point :')
             print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

             print("# School timing is from 08:30 am to 03:00 pm")
             print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
        elif cht==("YES"):
             bdp1=input('Enter your boarding point :')
             print("You have successfully registered to EDU Public School, our admission team will contact you soon... ")

             print("# School timing is from 08:30 am to 03:00 pm")
             print("# Special class timing for class 10, 11 and 12 is from 03:10 pm to 04:10 pm")
        else:
            print("Invalid entry")
if ch==2:
    adm=input("Enter your admission number :")
    print("1 = Fees\n2 = Transportation\n3 = Projects\n4 = Results")
    ch=int(input("Please enter your choice :"))
    if ch==1:
        class1= int(input("Enter the class : "))
        if class1<=5:
            print("The fees for class",class1," per term is : Rs 30,000")
        elif class1<=8:
            print("The fees for class",class1," per term is : Rs 40,000")
        elif class1<=10:
            print("The fees for class",class1," per term is : Rs 49,000")
        elif class1<=12:
            print("The fees for class",class1," per term is : Rs 60,000")
    elif ch==2:
        bdp=int(input('Enter the distance of your boarding point from school:'))
        if bdp<6:
            print("Your bus fees per term is Rs 8000")
        elif bdp<11:
            print("Your bus fees per term is Rs 15,000")
        elif bdp<21:
            print("Your bus fees per term is Rs 25,000")
        elif bdp<31:
            print("Your bus fees per term is Rs 36,000")
    elif ch==3:
        from datetime import date

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        print("No projects have been assigned to you till",d1)
    elif ch==4:
        from datetime import date

        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        print("No results have been published till",d1)
        
        

        
