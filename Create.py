import mysql.connector as mc

# connect to MySQL (create Project db if not exists)
con = mc.connect(host="localhost", user="root", passwd="root")
cur = con.cursor()

# create database if not exists
cur.execute("CREATE DATABASE IF NOT EXISTS Project")
cur.execute("USE Project")

# create school table
cur.execute("""
CREATE TABLE IF NOT EXISTS school (
    admno INT PRIMARY KEY,
    name VARCHAR(30),
    dob DATE,
    parent_name VARCHAR(30),
    parent_job VARCHAR(20),
    phone VARCHAR(15),
    class INT
)
""")

# create fees table
cur.execute("""
CREATE TABLE IF NOT EXISTS fees (
    admno INT,
    name VARCHAR(30),
    class INT,
    fee INT,
    FOREIGN KEY(admno) REFERENCES school(admno)
)
""")

con.commit()
cur.close()
con.close()
print("Database and tables created successfully.")
