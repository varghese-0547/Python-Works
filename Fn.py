def Add():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor
    _n=input('Name :')
    _dob=input('DOB :')
    _pn=input("Parent's name:")
    _pjob=input("Parent's job")
    _ph=int(input("Phno :"))
    _class
    n='select count(adnmo) from eduschool'
    cur.execute(n)
    nn=cur.fetchall()
    _rs=Addfees()
    q=f"insert into eduschool values(f'{nn+1001},'{_n}','{ _dob}', '{_pn}', '{_pjob}', {_ph} ,{_class})"
    q1=f"insert into FeeTable values({_admno},'{_n}', {_class},{_rs} )"
    cur.execute(q)
    cur.execute(q1)
    con.commit()
    cur.close()
    con.close()
##########################################################################################

def Login():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor
    q='select * from eduschool where admno={}'.format(_ADMNO)
    cur.execute(q)
    rs=cur.fetchall()
    cur.close()
    con.close()
    if _Admno not in rs:
        s='no'
    elif _Admno in rs:
        print(f'Welcome {rs[1]}')
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
    cur=con.cursor
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
    cur=con.cursor
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




