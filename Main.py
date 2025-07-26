from MFn import *
while True:
 
    print("\n===============================EDU Public School===============================")

    print("1 = Admission\n2 = Login")
    ch=int(input("Please enter your choice :"))
    if ch==1:
        print("Select the class",1,2,3,4,5,6,7,8,9,10)
        _class= int(input("Enter the class : "))
        if _class<=10:
            try:
                Add()
            except ModuleNotFoundError:
                print("Please install MySQL and import the required lib")
                continue

    if ch==2:
        _Admno=input("Enter your admission number :")
        s=Login(_Admno)
        
        if s=='NO':
            print("Invalid Admission number\nTry again")
            continue
        print("\nWelcome Mariyam\n")
        print("1 = Fees\n2 = Transportation\n3 = Projects\n4 = Edit Profile")
        ch=int(input("Please enter your choice :"))
        
        if ch==1:
            Fees()

        elif ch==3:
            Projects()

        elif ch==4:
            print("You can modify the following data")
            print("1 = Student name\n2 = DOB\n3 = Father name\n4 = Father job\n5 = Phno")
            _ch=int(input("Enter choice :"))
            Edit()














