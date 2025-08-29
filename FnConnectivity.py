import mysql.connector as mc
from pickle import *

def Con_cur():
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
    return con, cur

def Add(Class):
    con, cur = Con_cur()
    _n=input('Name :')
    _dob=input('DOB (YYYY-MM-DD) :')
    _pn=input("Parent's name:")
    _pjob=input("Parent's job:")
    _ph=int(input("Phno :"))
    Class

    n='SELECT COUNT(admno) FROM SCHOOL'
    cur.execute(n)
    nn=cur.fetchone()
    if nn[0] is None:
        User=1001
    else:
        User=nn[0]+1001
    Fee=Addfees(Class)
    q="INSERT INTO school VALUES(%s,%s,%s,%s,%s,%s,%s)"
    q1="INSERT INTO fees VALUES(%s,%s,%s,%s)"
    cur.execute(q,(User, _n, _dob, _pn, _pjob, _ph, Class))
    cur.execute(q1,(User, _n, Class, Fee))
    con.commit()
    cur.close()
    con.close()
    passwd=_n+'@'+str(User)
    d={User:passwd}
    fa=open("Login.dat","ab")
    dump(d,fa)
    fa.close()
    print("Data added successfully ")

def Login1(User):
    con, cur = Con_cur()
    cur.execute("SELECT * FROM school WHERE  admno = %s", (User,))
    rs=cur.fetchone()
    cur.close()
    con.close()
    if rs :
        return rs

def Login(User='Bob'):
    a=0
    while a<3:
        pd=input("Enter password :")
        with open("Login.dat","rb") as fr:
            try:
                while True :
                    stu = load(fr)
                    for k,v in stu.items():
                        if User=='Bob':
                            User="Admin"
                            if k == User and v == pd:
                                return True
                        if k == User and v == pd:
                            l = Login1(User)
                            return l[1]
                        else:
                            continue

                            
            except EOFError:
                pass
        a+=1
        print("Login/Password is wrong")
    print("Acces denied. Too many failed attempts.")
    return None
def Addfees(Class):
    if Class<=3:
        _fees=15000
    elif Class<=6:
        _fees=20000
    elif Class<=10:
        _fees=25000
    return _fees

def Fees(User):
    con, cur = Con_cur()
    q='SELECT admno, name, class, fee FROM fees WHERE admno=%s'
    cur.execute(q, (Admno,))
    rs=cur.fetchone()
    print(rs)
    cur.close()
    con.close()

def DisplayAll():
    con, cur = Con_cur()
    q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school'''
    cur.execute(q)
    rs=cur.fetchall()
    for i in rs:
        print(i)
    cur.close()
    con.close()

def Display(User):
    con, cur = Con_cur()
    q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE admno = %s'''
    cur.execute(q,(Admno,))
    rs=cur.fetchone()
    print(rs)
    cur.close()
    con.close()

def Projects():
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("No projects have been assigned to you till",d1)

def Results():
    from datetime import date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    print("No results have been published till",d1)

def Edit(User):
    con, cur = Con_cur()
    q1="SELECT * FROM school WHERE admno = %s"
    cur.execute(q1,(Admno,))
    rs=cur.fetchone()
    print(rs)
    if rs[0]==User:
        print("You can modify the following data")
        print("1 = Student name\n2 = DOB\n3 = Parent name\n4 = Parent job\n5 = Phone")
        _ch=input("Enter choice :")
        if _ch=='1':
            a=input("Enter student name :")
            q="UPDATE school SET name = %s WHERE admno = %s"
            cur.execute(q, (a,User))
            con.commit()
        elif _ch=='2':
            a=input("Enter new DOB :")
            q="UPDATE school SET bob = %s WHERE admno = %s"
            cur.execute(q, (a,User))
            con.commit()
        elif _ch=='3':
            a=input("Enter Parent name :")
            q="UPDATE school SET parent_name = %s WHERE admno = %s"
            cur.execute(q, (a,User))
            con.commit()
        elif _ch=='4':
            a=input("Enter Parent job :")
            q="UPDATE school SET parent_job = %s WHERE admno = %s"
            cur.execute(q, (a,User))
            con.commit()
        elif _ch=='5':
            a=input("Enter new Phno :")
            q="UPDATE school SET phone = %s WHERE admno = %s"
            cur.execute(q, (a,User))
            con.commit()
        cur.close()
        con.close()
        print("Successfully updated")

def Delete(User):
    con, cur = Con_cur()
    try:
        q1="DELETE FROM fees WHERE admno = %s"
        cur.execute(q1,(User,))
        q="DELETE FROM school WHERE admno = %s"
        cur.execute(q,(User,))
        con.commit()
        stu=[]
        n=[]
        found = False
        with open("Login.dat","rb") as fr:
            try:
                while True :
                    stu.append(load(fr))
            except EOFError:
                pass
            
        for i in stu :
            if User in i:
                print("Deleted :",i)
                found = True
            else:
                n.append(i)
        if found : 
            with open("Login.dat","wb") as fw:
                for i in n:
                    dump(i,fw)
        else:
            print("Record not found")
    except Exception as e :
        con.rollback()
        print("Error :",e)
        print("Try again later...")
    finally:
        cur.close()
        con.close()
