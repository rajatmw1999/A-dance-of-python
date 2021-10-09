import sqlite3

conn = sqlite3.connect("school.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS (
    admission_no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    standard INT
)
""")

cur.execute("INSERT INTO STUDENTS(admission_no, name, standard) VALUES (2, 'Rajat',13)")

data = cur.execute("SELECT * FROM STUDENTS")
print(data.fetchall())

conn.commit()

conn.close()