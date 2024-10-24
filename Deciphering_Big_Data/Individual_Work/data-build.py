import pandas as pd
import sqlite3

# Connect to SQLite Database
conn = sqlite3.connect('student_course_database.db')
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
students_df = pd.read_csv('students.csv')
students_df.to_sql('Students', conn, if_exists='replace', index=False)

courses_df = pd.read_csv('courses.csv')
courses_df.to_sql('Courses', conn, if_exists='replace', index=False)

teachers_df = pd.read_csv('teachers.csv')
teachers_df.to_sql('Teachers', conn, if_exists='replace', index=False)

student_courses_df = pd.read_csv('student_courses.csv')
student_courses_df.to_sql('Student_Courses', conn, if_exists='replace', index=False)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print('* Database saved *')