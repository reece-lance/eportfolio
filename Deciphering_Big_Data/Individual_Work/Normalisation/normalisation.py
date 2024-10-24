import pandas as pd

# Read the Excel File and strip extra spaces from column names
excel_file = 'Deciphering_Big_Data/Individual_Work/Normalisation/data/DBD_PCOM7E Table.xlsx'
df = pd.read_excel(excel_file)
df.columns = df.columns.str.strip()

# 1. Students Table
students_df = df[['Student Number', 'Student Name', 'Date of Birth', 'Exam Score', 'Support']].drop_duplicates()
students_df.columns = ['student_number', 'student_name', 'date_of_birth', 'exam_score', 'support']
students_df.to_csv('students.csv', index=False)

# 2. Courses Table (Course Name and Exam Board)
courses_df = df[['Course Name', 'Exam Boards']].drop_duplicates()
courses_df.columns = ['course_name', 'exam_board']
courses_df.to_csv('courses.csv', index=False)

# 3. Teachers Table (Course Name and Teacher Name)
teachers_df = df[['Course Name', 'Teacher Name']].drop_duplicates()
teachers_df.columns = ['course_name', 'teacher_name']
teachers_df.to_csv('teachers.csv', index=False)

# 4. Student-Courses Table (Student Number and Course Name)
student_courses_df = df[['Student Number', 'Course Name']].drop_duplicates()
student_courses_df.columns = ['student_number', 'course_name']
student_courses_df.to_csv('student_courses.csv', index=False)

print("CSV files have been created successfully!")
