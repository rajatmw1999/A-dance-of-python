# mysql
# mysql-connector-python
import mysql.connector

db = None
cursor = None


def getdata():
    print("Fetching the data from the db")
    query = "SELECT * FROM TEACHER"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    pass

def storedata():
    print("Storing some data in db")
    query = "INSERT INTO TEACHER VALUES (3,'Peter Baelish','Con Master')"
    cursor.execute(query)
    db.commit()

if __name__ == '__main__':
    db = mysql.connector.connect(user='sql6432654', password='mcsm5Uf6rx',
                                host='sql6.freemysqlhosting.net',
                                database='sql6432654')
    cursor = db.cursor()
    getdata()
    # storedata()
    db.close()