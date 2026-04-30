#1. import sqlite module to be able to use a database
import sqlite3

# 2. the connect method starts our database
connect = sqlite3.connect('testDb_p2.db')

#3. the cursor variable creates a new object that lets us send objects to our database
cursor = connect.cursor()

#4. we need to create a schema (structure) for our data
cursor.execute('''
    CREATE TABLE computers(
    id INTEGER PRIMARY KEY,
    model TEXT,
    color TEXT,
    hasWebcam BOOLEAN,
    memory INTEGER,
    price INTEGER
              
               )''')

cursor.execute('''
    INSERT INTO computers(model, color, hasWebcam, memory, price)
    VALUES('apple m4', 'blue', True, 8, 1500)
              ''')

cursor.execute('''
    INSERT INTO computers(model, color, hasWebcam, memory, price)
    VALUES('apple m4', 'blue', True, 8, 1500)
              ''')

cursor.execute('''
    INSERT INTO computers(model, color, hasWebcam, memory, price)
    VALUES('apple m1', 'red', True, 8, 1500)
              ''')


#update a computer
cursor.execute('''
    UPDATE computers
    SET color = 'yellow
    WHERE id = 3           
              ''')
        
connect.commit()
connect.close()