from BinFilesFn import *
while True:
    
    print("\n===============================EDU Public School===============================")

    print("1 = Admission\n2 = Login\n3 = Display all records\n4 = Edit Records")
    ch=input("Please enter your choice :")

    if ch=='1':
        print("Select the class",1,2,3,4,5,6,7,8,9,10)
        _class= int(input("Enter the class : "))
        if _class in range(1,11):
            _fees=Addfees(_class)
            Add(_class,_fees)
        else:
            print("Invalid Class\Try again")

    elif ch=='2':
        _Admno=int(input("Enter your admission number :"))
        p=Login(_Admno)
        if p==0:
            print("Invalid Admission number\nTry again")
            continue
        print("\nWelcome", p)
        print("1 = Fees\n2 = Projects")
        _ch=input("Please enter your choice :")
        if _ch=='1':
            Fees(_Admno)

        elif _ch=='2':
            Projects()
        else:
            print("Invalid choice")
    elif ch=='3':
        DisplayAll()

    elif ch=='4':
        Edit()
    else:
        print("\n\t\tINVALID CHOICE\n\t\t  TRY AGAIN")
        continue
    C=input("\n\nDo you wish to continue y/n:")
    if C in ['n','N','No','no',]:
        print("Have a nice day")
        break
