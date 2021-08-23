import mysql.connector

db = None
cursor = None

def fetchdata():
    cursor.execute("SELECT questions FROM gravity")
    data = cursor.fetchall()
    print(data)
    return data

def insertdata():
    question = input("Please enter a question : ")
    answer = input("Please enter an answer : ")
    existing_data = fetchdata()
    newlen = len(existing_data) + 1
    query = "INSERT INTO gravity VALUES({},'{}','{}')".format(newlen,question,answer)
    cursor.execute(query)
    db.commit()
    # print(cursor.lastrowid)
    fetchdata()

def createtable():
    query = "CREATE TABLE gravity(id INT, questions varchar(255), answers varchar(255))"
    cursor.execute(query)
    # db.commit()
    insertdata()

if __name__ == "__main__":
    try:
        db = mysql.connector.connect(user='', password='',
                                    host='',database='')
    except Exception as e:
        print(e)
    cursor = db.cursor()
    # fetchdata()
    # insertdata()
    createtable()