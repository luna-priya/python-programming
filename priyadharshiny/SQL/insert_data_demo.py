import sqlite3

try:
    connection = sqlite3.connect("Priya_DB.db")
    cursor = connection.cursor()
    insert_data_query = """
        INSERT INTO student (name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_data = ("Priyadharshiny", "priyadharshiny2007@gmail.com", "AIDS", "8.9")
    cursor.execute(insert_data_query, student_data)
    connection.commit()
    print("Student data inserted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()