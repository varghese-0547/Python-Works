from Fnconnectivity import *
while True:
    print("\n","="*30," EDU Public Schoo ","="*30)
    print("1 = Admin Login\n2 = Parent Login")
    c=input("Enter choice :")
    if c=='1':###ADMIN###
        a = Login()
        if a is not True:
            print("Invalid choice. Try again.")
            continue
        else:
            pass
        print("\n","="*30," Host  ","="*30)
        while True: 
            print("_"*55)
            print("-"*85)
            print('''\n0 = Log Out
1 = Admission
2 = Display records
3 = Search in records
4 = Edit Records
5=Delete Records''')
            print("_"*55)
            print("-"*85)
            ch=input("\nPlease enter your choice :")
            if ch=='1':
                while True:
                    print("-"*85)
                    print("\nSelect the class",1,2,3,4,5,6,7,8,9,10)
                    Class=input("\nEnter the class : ")
                    if Class in ['1','2','3','4','5','6','7','8','9','10']:
                        Class=int(Class)
                        Add(Class)
                        break
                    elif Class=='0' or Class in ['exit','Exit','EXIT']:
                        break
                    else :
                        print("Sorry choose a valid option")
            elif ch=='2':#Display
                print("-"*85)
                print('''\n1. Display all records\n2. Sort by Class
3. Sort by Date of Birth\n4. Sort by Date of Admission''')
                while True:
                    print("-"*85)
                    op=input("\nChoice :")
                    if op == '1':
                        Display()
                        break
                    elif op == '2':
                        Display('Class')
                        break
                    elif op =='3':
                        Display('DOB')
                        break
                    elif op=='4':
                        Display('S_DOA')
                        break
                    elif op=='0' or op in ['exit','Exit','EXIT']:
                        break
                    else:
                        print("Sorry choose a valid option")
            elif ch=='3':#Search
                print('''\n1. Search by Admno\n2. Search by Name\n3. Search by DOB
4. Search by Parent Name\n5. Search by Parent Job\n6. Search by Phone no
7.Search by Class\n8. Search by DOA''')
                while True:
                    print("-"*85)
                    op=input("\nChoice :")
                    if op == '1':
                        Search()
                        break
                    elif op == '2':
                        Search("Name")
                        break
                    elif op =='3':
                        Search("DOB")
                        break
                    elif op=='4':
                        Search("PN")
                        break
                    elif op=='5':
                        Search("PJ")
                        break
                    elif op=='6':
                        Search("Ph")
                        break
                    elif op=='7':
                        Search("Class")
                        break
                    elif op=='8':
                        Search()
                        break
                    elif op=='0' or op in ['exit','Exit','EXIT']:
                        break
                    else:
                        print("Sorry, choose a valid option")
                        
            elif ch=="4":#Edit
                print("-"*85)
                print("Step 1")
                while True:
                    print("\nStep 2")
                    User=input("\nEnter Admission number of\nthe record to be editted :")
                    print("\nStep 3")
                    if User.isdigit():
                        User=int(User)
                        print("\nStep 4")
                        print("\nStep 5")
                        if User=='0' or User in ['exit','Exit','EXIT']:
                            print("\nStep 6")
                            break
                        Edit(User)
                        break
                    else:
                        print("Sorry, enter a valid Admno")
                        continue
            elif ch=="5":#Delete
                print("-"*85)
                while True:
                    User=input("\nEnter Admission number of\nthe record to be deleted :")
                    if User.isdigit():
                        User=int(User)
                        
                        break
                    if User=='0' or User in ['exit','Exit','EXIT']:
                        break
                    else:
                        print("Sorry, enter a valid Admno")
                        continue
                    Delete(User)
                    break
            elif ch=='0':
                break
    if c=='2':#Login
        I=None
        while True:
            F='0'
            User=input("\nEnter your admission number :")
            if User=='0' or User in ['exit','Exit','EXIT']:
                F='1'
                break
            if User.isdigit():
                User=int(User)
                   
            else :
                print("Enter a valid Admno")
                continue
            I,N=Login(User)
            if I=='0':
                continue
            if I=='1':
                break
        if F != "1":
            while True:####Parent####
                print("\n","="*30," Parent ","="*30,"\n")
                print("Welcome",N)
                print("_"*55)
                print("-"*85)
                print("\n0 = Log Out\n1 = Fees\n2 = Projects\n3 = Display your details")
                ch=input("Please enter your choice :")
                if ch=='1':
                      Fees(User)
                elif ch=='2':
                     Projects()
                elif ch=='3':
                   Display(User)
                elif ch=='0' or ch in ['exit','Exit','EXIT']:
                    break
            
    if c=='0':
        break


