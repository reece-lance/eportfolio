import pandas as pd
import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect('Deciphering_Big_Data/Individual_Work/Data_Build/datastudent_course_database.db')
cursor = conn.cursor()

# Create Tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
    student_number INTEGER PRIMARY KEY,
    student_name TEXT,
    date_of_birth TEXT,
    exam_score INTEGER,
    support BOOLEAN
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    course_name TEXT PRIMARY KEY,
    exam_board TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Teachers (
    course_name TEXT,
    teacher_name TEXT,
    PRIMARY KEY (course_name, teacher_name),
    FOREIGN KEY (course_name) REFERENCES Courses(course_name)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Student_Courses (
    student_number INTEGER,
    course_name TEXT,
    PRIMARY KEY (student_number, course_name),
    FOREIGN KEY (student_number) REFERENCES Students(student_number) ON DELETE CASCADE,
    FOREIGN KEY (course_name) REFERENCES Courses(course_name)
)
''')

# Load data
students_df = pd.read_csv('Deciphering_Big_Data/Individual_Work/Normalisation/data/students.csv')
students_df.to_sql('Students', conn, if_exists='replace', index=False)

courses_df = pd.read_csv('Deciphering_Big_Data/Individual_Work/Normalisation/data/courses.csv')
courses_df.to_sql('Courses', conn, if_exists='replace', index=False)

teachers_df = pd.read_csv('Deciphering_Big_Data/Individual_Work/Normalisation/data/teachers.csv')
teachers_df.to_sql('Teachers', conn, if_exists='replace', index=False)

student_courses_df = pd.read_csv('Deciphering_Big_Data/Individual_Work/Normalisation/data/student_courses.csv')
student_courses_df.to_sql('Student_Courses', conn, if_exists='replace', index=False)

# Test the Database by querying

# Fetch all students
print("Students Table:")
for row in cursor.execute('SELECT * FROM Students'):
    print(row)

# Fetch all courses
print("\nCourses Table:")
for row in cursor.execute('SELECT * FROM Courses'):
    print(row)

# Fetch all teachers
print("\nTeachers Table:")
for row in cursor.execute('SELECT * FROM Teachers'):
    print(row)

# Fetch all student-course enrollments
print("\nStudent_Courses Table:")
for row in cursor.execute('SELECT * FROM Student_Courses'):
    print(row)

# Test: Delete a student and verify cascading deletes
def test_delete_student(conn):
    cursor = conn.cursor()

    # Deleting student with student_number = 1001 (Bob Baker)
    print("\nDeleting student with student_number = 1001 (Bob Baker)...")
    cursor.execute('DELETE FROM Students WHERE student_number = 1001')

    # Verify that the student's records were also removed from Student_Courses
    print("Checking if the student's course enrollments were deleted from Student_Courses...")
    cursor.execute('SELECT * FROM Student_Courses WHERE student_number = 1001')
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("Cascading delete successful. No course enrollments found for student 1001.")
    else:
        print("Cascading delete failed. There are still course enrollments for student 1001.")
    
    conn.commit()

# Run the delete test after the data is inserted
test_delete_student(conn)

conn.commit()
conn.close()

print('* Database saved *')
