from pickle import *
stu=[[1001, 'Jeyendu', '29-03-2008', 'Jayaram', 9446454105, 10, 25000], [1002, 'Mariya', '29-03-2008', 'John', 9446454105, 10, 25000],
[1003, 'Feba', '20-11-2008', 'Reji Paul', 9037078758, 10, 25000], [1004, 'Pooja', '29-03-2008', 'MG Muralidharan', 9496397607, 10, 25000]]
fw=open("Rec.dat","wb")
dump(stu,fw)
fw.close()
print("Data added successfully")

#   In write mode, the close() is not for saving the file but to move the file pointer back to (0,0)

def Add(_class,_fees):
    try :
        fr=open("Rec.dat","rb")
        stu=load(fr)
        ft=open("Rectemp.dat","wb")
        dump(stu,ft)
        L=len(stu)
        _rno=1001+L
        fr.close()
        ft.close()
    except FileNotFoundError:
        stu=[]
        _rno=1001
    except EOFError:
        stu=[]
        _rno=1001

    #f.close()
    print("Do not close the program while entering Data\nThe data you entered will be lost")
    print("If you enter any of your record incorrectly just submission")
    print("Go to the editting window to edit the records")
    print(_rno)
    _n=input('Name :')
    _dob=input('DOB :')
    _pn=input("Parent's name:")
    _ph=int(input("Phno :"))
    c=_class
    F=_fees
    print("If you enter any of your record incorrectly just submission")
    print("Go to the editting window to edit the records")
    s=input("Do you wish to continue submission :")
    if s in ['y','Y','yes','Yes','YES']:
        data=[_rno,_n,_dob,_pn,_ph,c,F]
        
        stu.append(data)
      
        with open("Rec.dat","wb") as fw:
            dump(stu,fw)
        print("Data added successfully ")
        
#Add(10,25000)

##########################################################################################

def Login():
    with open("Rec.dat","rb") as fr:
        stu=load(fr)
        m=0
        r=int(input("Enter Roll no. :"))
        L=[]
        for i in stu:
            L.append(i[0])
            if i[0]==r:
                m=1
                print("Welcome",i[1])
        if m==0:
            print("Record not found")
#Login()
     
##########################################################################################
def Display():

    fr=open("Rec.dat","rb")
    fr.seek(0)
    stu=load(fr)
    for i in stu:
        print(i[0],i[1])
    fr.close()
#Display()


##########################################################################################
#   If you call this fn() it will initially erase all data, so /Beware
def Edit():
    print("*****Edit*****\n")
    Display()
    fr=open("Rec.dat","rb")
    stu=load(fr)
    ft=open("Rectemp.dat","wb")
    dump(stu,ft)
    fw=open("Rec.dat","wb")
    c=input("Do you wish to continue :")
    if c in ['y','Y','yes','Yes','YES'] :
        r=int(input("Enter Roll no :"))
        for i in stu:
            if i[0]==r:
                print(i)
        print("1 Edit Name")
        print("2 Edit DOB")
        print("3 Edit Father Name")
        print("4 Phno")
        print("5 Edit Class")
        _ch=int(input("Enter choice :"))

        for i in stu:
            if i[0]==r:

                if _ch==1:
                    a=input("Enter name :")
                    i[1]=a
                elif _ch==2:
                    a=input("Enter new DOB :")
                    i[2]=a
                elif _ch==3:
                    a=input("Enter Father name:")
                    i[3]=a
                elif _ch==4:
                    a=int(input("Enter Phno :"))
                    i[4]=a
                elif _ch==5:
                    a=int(input("Enter Class :"))
                    i[5]=a
                break
        print("Successfully updated")
    dump(stu,fw)
    fr.close()
    ft.close()
    fw.close()
Edit()
    
##########################################################################################
def Addfees(_class):
    if _class<=3:
        _fees=15000
    elif _class<=6:
        _fees=20000
    elif _class<=10:
        _fees=25000
    return _fees
##########################################################################################

def Fees():
    print(_fees)
##########################################################################################

def Projects():
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("No projects have been assigned to you till",d1)
##########################################################################################

def Results():
    from datetime import date

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("No results have been published till",d1)

