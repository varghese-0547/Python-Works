import mysql.connector as mc
from pickle import *
from tabulate import tabulate
from datetime import date
def Date():
    global d1
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")
def Con_cur():
    con=mc.connect(host='localhost', user='root', passwd='root', database='eduschool')
    cur=con.cursor()
    return con, cur
def Add(Class):
    con, cur = Con_cur()
    _n=input('Name :')
    _dob=input('DOB (YYYY-MM-DD) :')
    _pn=input("Parent's name:")
    _pjob=input("Parent's job:")
    _ph=int(input("Phno :"))
    Date()  # Get current date for DOA
    n='SELECT MAX(admno) FROM SCHOOL'
    cur.execute(n)
    nn=cur.fetchone()
    if nn[0] is None:
        User=1001
    else:
        User=nn[0]+1
    Fee=Addfees(Class)
    q="INSERT INTO school VALUES(%s,%s,%s,%s,%s,%s,%s)"
    q1="INSERT INTO fees VALUES(%s,%s,%s,%s,%s)"
    cur.execute(q,(User, _n, _dob, _pn, _pjob, _ph, Class))
    cur.execute(q1,(User, _n, Class, Fee, d1))  # Added d1 for DOA
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

def Login(User="Bob"):
    
        
    a=0
    while a<3:

        pd=input("Enter password :")
        if pd=='0':
            return "0","False"
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
                            return '1',l[1]
                        else:
                            
                            continue
            
            except EOFError:
                pass

        a+=1
        print("Login/Password is wrong\nTry again")
    print("Acces denied. Too many failed attempts.")
    return "0","False"
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
    q='SELECT admno, name, class, fee, DATE_FORMAT(doa, \'%d-%m-%Y\') FROM fees WHERE admno=%s'
    cur.execute(q, (User,))
    rs=cur.fetchone()
    if rs:
        h=['Admno','Name','Class','Fee','Date of Admission']
        print(tabulate([rs],headers=h,tablefmt="rounded_grid"))
    else:
        print("No fee record found")
    cur.close()
    con.close()

def Display(User='A'):
    con, cur = Con_cur()
    if User=='A':#Display all
        q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class, doa FROM school NATURAL JOIN FEES'''
        cur.execute(q)
        rs=cur.fetchall()
        h=['Admno','Name','DOB','Parent Name','Parent Job','Phone no','Class','DOA']
        print(tabulate(rs,headers=h,tablefmt="rounded_grid"))
    if User == 'Class':#Order by Class
        q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school ORDER BY class'''
        cur.execute(q)
        rs=cur.fetchall()
        h=['Admno','Name','DOB','Parent Name','Parent Job','Phone no','Class']
        print(tabulate(rs,headers=h,tablefmt="rounded_grid"))
    if User == 'DOB':#Order by DOB
        q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school ORDER BY dob'''
        cur.execute(q)
        rs=cur.fetchall()
        h=['Admno','Name','DOB','Parent Name','Parent Job','Phone no','Class']
        print(tabulate(rs,headers=h,tablefmt="rounded_grid"))
    if User == 'S_DOA':#Order by DOA
        q='''SELECT fees.admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class, doa FROM school NATURAL JOIN FEES ORDER BY doa'''
        cur.execute(q)
        rs=cur.fetchall()
        h=['Admno','Name','DOB','Parent Name','Parent Job','Phone no','Class','DOA' ]
        print(tabulate(rs,headers=h,tablefmt="rounded_grid"))

    if type(User) is int:#Display fn for parent
        q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE admno = %s'''
        cur.execute(q,(User,))
        rs=cur.fetchone()
        h=[{'Admno':rs[0]},{'Name':rs[1]},{'DOB':rs[2]},{'Parent Name':rs[3]},
           {'Parent Job':rs[4]},{'Phone no':rs[5]},{'Class':rs[6]}]
        for i in h:
           print(i)
    cur.close()
    con.close()
##Display('C')
def Search(User='Admno'):
    con, cur = Con_cur()
    while True:
        if User=='Admno':
            n=input("\nEnter the Admno to be checked :")
            if n.isdigit():#Search by Admno
                q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE Admno = %s'''
                cur.execute(q,(n,))
                rs=cur.fetchall()
        elif User=='Name':#Search by Name
            n=input("\nEnter the Name to be checked :")
            if n.isalpha():
                q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE name = %s'''
                cur.execute(q,(n,))
                rs=cur.fetchall()
        elif User=='DOB':#Search by DOB
            n=input("\nEnter the DOB to be checked :")
            q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE dob = %s'''
            cur.execute(q,(n,))
            rs=cur.fetchall()
        elif User=='PN':#Search by Parent name
            n=input("\nEnter the Parent Name to be checked :")
            if n.isalpha():
                q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE parent_name = %s'''
                cur.execute(q,(n,))
                rs=cur.fetchall()

        elif User=='PJ':#Search by Parent Job
            n=input("\nEnter the Parent Job to be checked :")
            if n.isalpha():
                q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE parent_job = %s'''
                cur.execute(q,(n,))
                rs=cur.fetchall()
        elif User=='Ph':#Search by Phone no
            n=input("\nEnter the Phone no to be checked :")
            if n.isdigit():
                q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE phone = %s'''
                cur.execute(q,(n,))
                rs=cur.fetchall()
        elif User=='Class':#Search by Class
            n=input("\nEnter the Class to be checked :")
            if n.isdigit():
                q='''SELECT admno, name, DATE_FORMAT(dob, '%d-%m-%Y'),
parent_name, parent_job, phone, class FROM school WHERE class = %s'''
                cur.execute(q,(n,))
                rs=cur.fetchall()
        if rs:
            h=['Admno','Name','DOB','Parent Name','Parent Job','Phone no','Class']
            print(tabulate(rs,headers=h,tablefmt="rounded_grid"))
            break
        else:
            print("Record not found\nTry again")
    cur.close()
    con.close()

def Projects():
    Date()
    print("No projects have been assigned to you till",d1)
def Results():
    Date()
    print("No results have been published till",d1)

def Edit(User):
    con, cur = Con_cur()
    q1="SELECT * FROM school WHERE admno = %s"
    cur.execute(q1,(User,))
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
            # Also update name in fees table
            q2="UPDATE fees SET name = %s WHERE admno = %s"
            cur.execute(q2, (a,User))
            con.commit()
        elif _ch=='2':
            a=input("Enter new DOB :")
            q="UPDATE school SET dob = %s WHERE admno = %s"
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
