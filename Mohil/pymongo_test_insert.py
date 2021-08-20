def get_database():
    from pymongo import MongoClient
    import pymongo

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = "mongodb+srv://rajatmw1999:mycampk12db@cluster0.mw802.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    db = client.database
    collection = db.AtomsandMolecules

    emp_rec1 = {
        "name":"Mr.Geek",
        "eid":24,
        "location":"delhi"
        }
    emp_rec2 = {
            "name":"Mr.Shaurya",
            "eid":14,
            "location":"delhi"
            }
  
    # Insert Data
    rec_id1 = collection.insert_one(emp_rec1)
    rec_id2 = collection.insert_one(emp_rec2)
  
    print("Data inserted with record ids",rec_id1," ",rec_id2)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['user_shopping_list']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()