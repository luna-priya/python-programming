import sqlite3

try:
    connection = sqlite3.connect("Priya_DB.db")
    cursor = connection.cursor()
    delete_query = "DELETE FROM student WHERE rollno = ?"
    delete_values = (1,)
    cursor.execute(delete_query, delete_values)
    connection.commit()
    print("Student deleted Successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()
