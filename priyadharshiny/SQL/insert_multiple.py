import sqlite3

try:
    connection = sqlite3.connect("Priya_DB.db")
    cursor = connection.cursor()
    insert_data_query = """
        INSERT INTO student (name,email,course,cgpa) VALUES (?,?,?,?)
        """
    student_records = [
        ("Krishan", "krishan@gmail.com", " ECE", 7.8),
        ("chitra", "chitra@gmail.com", "AIML", 6.9),
        ("Prakash", "prakash@gmail.com", "AIDS", 8.9),
        ("Kaviths", "kavitha@gmail.com", "EEE", 8.8)
    ]
    cursor.executemany(insert_data_query, student_records)
    connection.commit()
    print("aLL Student Recoreds inserted successfully")
except sqlite3.Error as error:
    print(error)
finally:
    cursor.close()
    connection.close()