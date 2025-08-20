import sqlite3

# connect to sqlite database (creates file if not exists)
con = sqlite3.connect("EDU_School.db")
cur = con.cursor()

# create student table
cur.execute("""
CREATE TABLE IF NOT EXISTS eduschool (
    admno INTEGER PRIMARY KEY,
    name TEXT,
    dob TEXT,
    parent_name TEXT,
    parent_job TEXT,
    phone INTEGER,
    class TEXT
)
""")

# create fee table
cur.execute("""
CREATE TABLE IF NOT EXISTS FeeTable (
    admno INTEGER,
    name TEXT,
    class TEXT,
    fee INTEGER,
    FOREIGN KEY(admno) REFERENCES eduschool(admno)
)
""")

con.commit()
con.close()
