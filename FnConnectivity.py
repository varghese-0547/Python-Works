import mysql.connector as mc
from pickle import *


def Add(Class):
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
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
        Admno=1001
    else:
        Admno=nn[0]+1001
    Fee=Addfees(Class)
    q="INSERT INTO school VALUES(%s,%s,%s,%s,%s,%s,%s)"
    q1="INSERT INTO fees VALUES(%s,%s,%s,%s)"
    cur.execute(q,(Admno, _n, _dob, _pn, _pjob, _ph, Class))
    cur.execute(q1,(Admno, _n, Class, Fee))
    con.commit()
    cur.close()
    con.close()
    passwd=_n+'@'+str(Admno)
    d={Admno:passwd}
    fa=open("Login.dat","ab")
    dump(d,fa)
    fa.close()
    print("Data added successfully ")

def Login1(Admno):
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
    cur.execute("SELECT * FROM school WHERE  admno = %s", (Admno,))
    rs=cur.fetchone()
    cur.close()
    con.close()
    if rs :
        return rs

def Login(Admno,pd):

    with open("Login.dat","rb") as fr:
        try:
            while True :
                stu = load(fr)
                for k,v in stu.items():
                    if k == Admno and v == pd:
                        l = Login1(Admno)
                        return l[1]

        except EOFError:
            pass
    print("Login/Password is wrong")
    return None
def Addfees(Class):
    if Class<=3:
        _fees=15000
    elif Class<=6:
        _fees=20000
    elif Class<=10:
        _fees=25000
    return _fees

def Fees(Admno):
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
    q='SELECT admno, name, class, fee FROM fees WHERE admno=%s'
    cur.execute(q, (Admno,))
    rs=cur.fetchone()
    print(rs)
    cur.close()
    con.close()

def DisplayAll():
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
    q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school'''
    cur.execute(q)
    rs=cur.fetchall()
    for i in rs:
        print(i)
    cur.close()
    con.close()

def Display(Admno):
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
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

def Edit(Admno):
    con = mc.connect(host='localhost', user='root', passwd='root', database='project')
    cur = con.cursor()
    q1="SELECT * FROM school WHERE admno = %s"
    cur.execute(q1,(Admno,))
    rs=cur.fetchone()
    print(rs)
    if rs[0]==Admno:
        print("You can modify the following data")
        print("1 = Student name\n2 = DOB\n3 = Parent name\n4 = Parent job\n5 = Phone")
        _ch=input("Enter choice :")
        if _ch=='1':
            a=input("Enter student name :")
            q="UPDATE school SET name = %s WHERE admno = %s"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='2':
            a=input("Enter new DOB :")
            q="UPDATE school SET bob = %s WHERE admno = %s"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='3':
            a=input("Enter Parent name :")
            q="UPDATE school SET parent_name = %s WHERE admno = %s"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='4':
            a=input("Enter Parent job :")
            q="UPDATE school SET parent_job = %s WHERE admno = %s"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='5':
            a=input("Enter new Phno :")
            q="UPDATE school SET phone = %s WHERE admno = %s"
            cur.execute(q, (a,Admno))
            con.commit()
        cur.close()
        con.close()
        print("Successfully updated")

def Delete(Admno):
    con = mc.connect(host='localhost', user='root', passwd='root', database='Project')
    cur = con.cursor()
    try:
    
        q1="DELETE FROM fees WHERE admno = %s"
        cur.execute(q1,(Admno,))
        q="DELETE FROM school WHERE admno = %s"
        cur.execute(q,(Admno,))
        con.commit()
        print("Successfully Deleted")
    except Exception as e :
        con.rollback()
        print("Error :",e)
        print("Try again later...")
    finally:
        cur.close()
        con.close()
