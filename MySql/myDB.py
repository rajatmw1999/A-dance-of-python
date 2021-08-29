from logging import currentframe
import mysql.connector
import datetime

class myDB:
    def __init__(self,username, password, host, database):
        self.db = None
        self.cursor = None
        try:
            self.db = mysql.connector.connect(user=username, password=password,
                                    host=host,database=database)
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e)
        self.initializeDB()
        return None
    
    def initializeDB(self):
        query = "CREATE TABLE IF NOT EXISTS python(id INT, question varchar(500), answer varchar(500), author varchar(255), added_by varchar(255), created_at DATETIME)"
        self.executeQuery(query)
    
    def executeQuery(self,query):
        try:
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    def fetchData(self, query):
        self.executeQuery(query)
        return self.cursor.fetchall()
    
    def insertData(self,tableName, question, answer, author, added_by):
        try:
            currentData = self.fetchData("SELECT * FROM {}".format(tableName))
            query = "INSERT INTO {} VALUES ('{}','{}','{}','{}','{}','{}')".format(tableName, len(currentData) + 1,question,answer,author,added_by,datetime.datetime.now())
            print(query)
            self.cursor.execute(query)
            self.db.commit()
        except Exception as e:
            print(e)
       
        
mydb1 = myDB('root','rajat@1999','127.0.0.1','notes')
mydb1.insertData('python','hey','hello','hi','bye')