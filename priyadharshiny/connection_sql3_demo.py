import sqlite3

try:
    #connect to the database
    connection=sqlite3.connect('Priya_DB.db')
    cursor=connection.cursor()
    #select and print data
    cursor.execute("SELECT * FROM book")
    print("book in the database: ")
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"SQlite error:{e}")
finally:
    if connection:
        connection.close()
