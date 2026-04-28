#1. import sqlite module to be able to use a database
import sqlite

# 2. the connect method starts our database
connect = sqlite.connect()

#3. the cursor variable creates a new object that lets us send objects to our database
cursor = connect.cursor()

#4. we need to create a schema (structure) for our data
cursor.excute('''
    CREATE TABLE computers(
    id INTEGER PRIMARY KEY,
    model TEXT,
    color TEXT,
    hasWebcam BOOLEAN,
    memory INTEGER
    price INTEGER
    
               )''')