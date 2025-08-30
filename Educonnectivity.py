from Fnconnectivity import *
while True:
    
    print("\n===============================EDU Public School===============================")

    print("1 = Admin Login\n2 = Parent Login")
    c=input("Enter choice :")
    if c=='1':
        a = Login()
        if a is not True:
            print("Invalid choice. Try again.")
            continue
        else:
            pass
    
            
            
        print("\n===============================  Host  ===============================")
        while True:
            print('''\n\n0 = Log Out
1 = Admission
2 = Display all records
3 = Display fee records
4 = Edit Records
5=Delete Records''')
            ch=input("Please enter your choice :")
            if ch=='1':
                print("Select the class",1,2,3,4,5,6,7,8,9,10)
                Class= int(input("Enter the class : "))
                if Class<=10:
                    try:
                        Add(Class)
                    except ModuleNotFoundError:
                        print("Please install MySQL and import the required lib")
                        continue
            elif ch=='2':
                Display()
            elif ch=='3':
                print("Fn on progress")
            elif ch=='4':
                User=int(input("\nEnter Admission number of\nthe record to be editted :"))
                Edit(User)
            elif ch=='5':
                User=int(input("\nEnter Admission number of\nthe record to be deleted :"))
                Delete(User)
            elif ch=='0':
                break
            

    if c=='2':
        User=int(input("Enter your admission number :"))
        I=Login(User)
        if I is None:
            print("Try again\n")
            continue
        while True:
            print("\n=============================== Parent ===============================\n")
            print("Welcome",I)
            print("\n\n0 = Log Out\n1 = Fees\n2 = Projects\n3 = Display your details")
            ch=input("Please enter your choice :")
            if ch=='1':
                  Fees(User)
            elif ch=='2':
                 Projects()
            elif ch=='3':
               Display(User)
            elif ch=='0':
                break
            
    if c=='0':
        break
