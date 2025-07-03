def Fees():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor
    q='select admno, name, class, fees from T1 where admno={}'.format(_ADMNO)
    cur.execute(q)
    rs=cur.fetchall()
    print(rs)
    cur.close()
    con.close()
##########################################################################################

def Trnspt():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor
    q='select * from T1 where admno={}'.format(_ADMNO)
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
def Add():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor
    _n=input('Name :')
    _dob=input('DOB :')
    _fn=input("Father's name:")
    _fjob=input("Father's job")
    _ph=int(input("Phno :"))
    
    n='select count(adnmo) from eduschool'
    cur.execute(n)
    nn=cur.fetchall()
    q=f"insert into T1 values(f'{nn+1001},{_n},{ _dob}, {_fn}, {_fjob}, {_ph} )"
    cur.execute(q)
    con.commit()
    cur.close()
    con.close()
##########################################################################################
def Login():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passwd='root',database='EDU_School')
    cur=con.cursor
    q='select * from T1 where admno={}'.format(_ADMNO)
    cur.execute(q)
    rs=cur.fetchall()
    cur.close()
    con.close()
    if _Admno not in rs:
        s='no'
    elif _Admno in rs:
        print(f'Welcome {rs[1]}')
