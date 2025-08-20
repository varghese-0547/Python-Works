import sqlite3
def Add(Class):
    
    con = sqlite3.connect("EDU_School.db")
    cur = con.cursor()
    _n=input('Name :')
    _dob=input('DOB :')
    _pn=input("Parent's name:")
    _pjob=input("Parent's job")
    _ph=int(input("Phno :"))
    Class

    n='select count(admno) from eduschool'
    cur.execute(n)
    nn=cur.fetchone()
    Admno=nn[0]+1001
    Fee=Addfees(Class)
    q="insert into eduschool values(?,?,?,?,?,?,?)"
    q1="insert into FeeTable values(?,?,?,?)"
    cur.execute(q,(Admno, _n, _dob, _pn, _pjob, _ph, Class))
    cur.execute(q1,(Admno, _n, Class, Fee))
    con.commit()
    cur.close()
    con.close()
    print("Data added successfully ")

def Login(Admno):
    con = sqlite3.connect("EDU_School.db")
    cur = con.cursor()
    q='select * from eduschool where admno=?'
    cur.execute(q, (Admno,))
    rs=cur.fetchall()
    cur.close()
    con.close()
    for i in rs:
        if i[0]==Admno:
            return i

def Addfees(Class):
    if Class<=3:
        _fees=15000
    elif Class<=6:
        _fees=20000
    elif Class<=10:
        _fees=25000
    return _fees

def Fees(Admno):

    con = sqlite3.connect("EDU_School.db")
    cur = con.cursor()
    q='select admno, name, class, fee from FeeTable where admno=?'
    cur.execute(q, (Admno,))
    rs=cur.fetchall()
    print(rs)
    cur.close()
    con.close()

def DisplayAll():

    con = sqlite3.connect("EDU_School.db")
    cur = con.cursor()
    q="select * from EDUSCHOOL"
    cur.execute(q)
    rs=cur.fetchall()
    for i in rs:
        print(i)
    cur.close()
    con.close()

def Display(Admno):

    con = sqlite3.connect("EDU_School.db")
    cur = con.cursor()
    q="select * from EDUSCHOOL where ADMNO = ?"
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

    con = sqlite3.connect("EDU_School.db")
    cur = con.cursor()
    q1="select * from EDUSCHOOL where admno=?"
    cur.execute(q1,(Admno,))
    rs=cur.fetchone()
    print(rs)
    if rs[0]==Admno:
        print("You can modify the following data")
        print("1 = Student name\n2 = DOB\n3 = Parent name\n4 = Parent job\n5 = Phone")
        _ch=input("Enter choice :")
        if _ch=='1':
            a=input("Enter student name :")
            q="update EDUSCHOOL set NAME = ? where ADMNO = ?"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='2':
            a=input("Enter new DOB :")
            q="update EDUSCHOOL set DOB = ? where ADMNO = ?"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='3':
            a=input("Enter Parent name :")
            q="update EDUSCHOOL set PARENT_NAME = ? where ADMNO = ?"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _ch=='4':
            a=input("Enter Parent job :")
            q="update EDUSCHOOL set PARENT_JOB = ? where ADMNO = ?"
            cur.execute(q, (a,Admno))
            con.commit()
        elif _che=='5':
            a=input("Enter new Phno :")
            q="update EDUSCHOOL set PHONE = ? where ADMNO = ?"
            cur.execute(q, (a,Admno))
            con.commit()
        cur.close()
        con.close()
        print("Successfully updated")
