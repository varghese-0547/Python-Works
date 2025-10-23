from Fnconnectivity import *
while True:
    print("\n","="*16," EDU Public Schoo ","="*16)
    print("1 = Admin Login\n2 = Parent Login")
    c=input("Enter choice :")
    if c=='1':###ADMIN###
        a = Login()
        if a is not True:
            #print("Invalid choice. Try again.")
            continue
        if a is None:
            continue
        else:
            pass
        print("\n","="*22,"Host","="*22)
        while True: 
            print("="*50)
            print('''\n0 = Log Out
1 = Admission
2 = Display records
3 = Search in records
4 = Edit Records
5=Delete Records''')
            print("="*50)
            ch=input("\nPlease enter your choice :")
            if ch=='1':
                while True:
                    print("="*50)
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
                print("="*50)
                print('''\n1. Display all records\n2. Sort by Class
3. Sort by Date of Birth\n4. Sort by Date of Admission''')
                while True:
                    print("="*50)
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
                X=''
                while True:
                    print('''\n1. Search by Admno\n2. Search by Name\n3. Search by DOB
4. Search by Parent Name\n5. Search by Parent Job\n6. Search by Phone no
7.Search by Class\n8. Search by DOA''')
                    print("="*50)
                    op=input("\nChoice op:")
                    if op == '1':
                        X=Search()
                        
                    elif op == '2':
                        X=Search("Name")
                        
                    elif op =='3':
                        X=Search("DOB")
                        
                    elif op=='4':
                        X=Search("PN")
                        
                    elif op=='5':
                        X=Search("PJ")
                        
                    elif op=='6':
                        X=Search("Ph")
                        
                    elif op=='7':
                        X=Search("Class")
                        
                    elif op=='8':
                        X=Search("DOA")
                        
                    elif op=='0' or op in ['exit','Exit','EXIT']:
                        break
                        
                    else:
                        print("Sorry, choose a valid option")
                    if X=="CONTINUE":
                        continue
                    break
                print(X)
            elif ch=="4":#Edit
                print("="*50)
                while True:
                    User=input("\nEnter Admission number of\nthe record to be editted :")
                    if User=='0' or User in ['exit','Exit','EXIT']:
                        break
                    if User.isdigit():
                        User=int(User)
                        print(Edit(User))
                        break
                    else:
                        print("Sorry, enter a valid Admno")
                        continue
            elif ch=="5":  # Delete
                print("="*50)
                a=''
                while True:
                    if '0' in a:
                        break
                    a=Login()
                    if (a is not True) or (a is None)  :
                        continue
                    
                    else:
                        pass
                    User = input("\nEnter Admission number of\nthe record to be deleted: ")
                    if User == '0' or User in ['exit', 'Exit', 'EXIT']:
                        print("Nothing was deleted")
                        break
                    sure=input("Are you sure y/n: ")
                    if sure not in ['y','Y','yes','Yes','YES']:
                        print("Nothing was deleted")
                        break
                    if User.isdigit():
                        User = int(User)
                        Delete(User)
                        print("Successfully Deleted")
                        break

                    else:
                        print("Sorry, enter a valid Admno")
                        continue
            elif ch=='0' or ch in ['exit', 'Exit', 'EXIT']:  #HOST
                break
            else:
                print("Invalid choice. Please try again.")     

    if c=='2':#PARENT
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
            if I=='1' :
                break
        if F != "1":
            print("\n","="*21," Parent ","="*21,"\n")
            print("Welcome",N)
            while True:####Parent####
                print("="*50)
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
                print("\n","="*21," Parent ","="*21,"\n")
            
    if c=='0':
        break


