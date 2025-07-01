def Fees():
    import mysql.connector as mc
    con=mc.connect(host='localhost',user='root',passdw='root',database='EDUSchool')
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
    con=mc.connect(host='localhost',user='root',passdw='root',database='EDUSchool')
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
    con=mc.connect(host='localhost',user='root',passdw='root',database='EDUSchool')
    cur=con.cursor
    _n=input()
    _dob=input()
    _fn=input()
    _mn=input()
    _ph=int(input())
    _adrs=input()
    q="insert into T1 values(f'{_n},{ _dob}, {_fn}, {_mn}, {_ph}, {_adrs} )"
    cur.execute(q)
    con.commit()
    cur.close()
    con.close()
























