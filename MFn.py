'''
def Add():
    _n=input('Name :')
    _dob=input('DOB :')
    _pn=input("Parent's name:")
    _pjob=input("Parent's job")
    _ph=int(input("Phno :"))
    _class
    #with open("Rec.txt","a") as f:
        

    print("Data added successfully ")
'''
##########################################################################################

def Login(_Admno):
    with open("Rec.txt","r") as f:
        l=len(f.readlines())
        s=''
        for i in range(0,l,7):
            f.seek(0)
            s+=f.readlines()[i]
            
        if _Admno not in s:
            return 'NO'

            




'''
##    if _Admno not in rs:
##        s='no'
##    elif _Admno in rs:
##        print(f'Welcome {rs[1]}')
##########################################################################################
def Addfees():
    
    if _class<=3:
        _fees=15000
    elif _class<=6:
        _fees=20000
    elif _class<=10:
        _fees=25000
    return _fees
##########################################################################################

def Fees():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor()
    q='select admno, name, class, fees from FeeTable where admno={}'.format(_ADMNO)
    cur.execute(q)
    rs=cur.fetchall()
    print(rs)
    cur.close()
    con.close()
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
##########################################################################################
def Edit():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor()
    if _ch==1:
        a=input("Enter name :")
        q="update eduschool set name = '{a}' where admno = {_Admno}")
        cur.execute(q)
        con.commite()
    elif _ch==2:
        a=input("Enter new DOB :")
        q="update eduschool set name = '{a}' where admno = {_Admno}")
        cur.execute(q)
        con.commite()
    elif _ch==3:
        a=input("Enter Father name:")
        q="update eduschool set name = '{a}' where admno = {_Admno}")
        cur.execute(q)
        con.commite()
    elif _ch==4:
        a=input("Enter Father job:")
        q="update eduschool set name = '{a}' where admno = {_Admno}")
        cur.execute(q)
        con.commite()
    elif _ch==5:
        a=input("Enter new Phno :")
        q="update eduschool set name = '{a}' where admno = {_Admno}")
        cur.execute(q)
        con.commite()
    cur.close()
    con.close()
    print("Successfully updated")
'''


