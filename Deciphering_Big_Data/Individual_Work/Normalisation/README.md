# Normalisation

## Task Description
This task involved normalising un-normalised data related to students, their courses, teachers, and exam boards. The objective was to organise the data into 3rd Normal Form (3NF) by eliminating repeating groups, partial dependencies, and transitive dependencies. The process was carried out in three steps: 1NF, 2NF, and 3NF, with each step focusing on reducing redundancy and ensuring data integrity.

---

## 1NF - First Normal Form
In 1NF, repeating groups were removed by making sure all attributes had atomic values.
  
| Student Number | Student Name  | Exam Score | Support | Date of Birth | Course Name      | Exam Board | Teacher Name |
|----------------|---------------|------------|---------|---------------|------------------|------------|--------------|
| 1001           | Bob Baker     | 78         | No      | 25/08/2001    | Computer Science | BCS        | Mr Jones     |
| 1001           | Bob Baker     | 78         | No      | 25/08/2001    | Maths            | EdExcel    | Ms Parker    |
| 1001           | Bob Baker     | 78         | No      | 25/08/2001    | Physics          | OCR        | Mr Peters    |
| 1002           | Sally Davies  | 55         | Yes     | 02/10/1999    | Maths            | AQA        | Ms Parker    |
| 1002           | Sally Davies  | 55         | Yes     | 02/10/1999    | Biology          | WJEC       | Mrs Patel    |
| 1002           | Sally Davies  | 55         | Yes     | 02/10/1999    | Music            | AQA        | Ms Daniels   |
| 1003           | Mark Hanmill  | 90         | No      | 05/06/1995    | Computer Science | BCS        | Mr Jones     |
| 1003           | Mark Hanmill  | 90         | No      | 05/06/1995    | Maths            | EdExcel    | Ms Parker    |
| 1003           | Mark Hanmill  | 90         | No      | 05/06/1995    | Physics          | OCR        | Mr Peters    |
| 1004           | Anas Ali      | 70         | No      | 03/08/1980    | Maths            | AQA        | Ms Parker    |
| 1004           | Anas Ali      | 70         | No      | 03/08/1980    | Physics          | OCR        | Mr Peters    |
| 1004           | Anas Ali      | 70         | No      | 03/08/1980    | Biology          | WJEC       | Mrs Patel    |
| 1005           | Cheuk Yin     | 45         | Yes     | 01/05/2002    | Computer Science | BCS        | Mr Jones     |
| 1005           | Cheuk Yin     | 45         | Yes     | 01/05/2002    | Maths            | EdExcel    | Ms Parker    |
| 1005           | Cheuk Yin     | 45         | Yes     | 01/05/2002    | Music            | AQA        | Ms Daniels   |

---

## 2NF - Second Normal Form
In 2NF, partial dependencies were removed by splitting the data into two tables: one for student-specific details and one for course-related information.
  
### Students Table
| Student Number | Student Name   | Date of Birth | Exam Score | Support |
|----------------|----------------|---------------|------------|---------|
| 1001           | Bob Baker      | 25/08/2001    | 78         | No      |
| 1002           | Sally Davies   | 02/10/1999    | 55         | Yes     |
| 1003           | Mark Hanmill   | 05/06/1995    | 90         | No      |
| 1004           | Anas Ali       | 03/08/1980    | 70         | No      |
| 1005           | Cheuk Yin      | 01/05/2002    | 45         | Yes     |
  
### Student_Courses Table
| Student Number | Course Name      | Exam Board | Teacher Name |
|----------------|------------------|------------|--------------|
| 1001           | Computer Science | BCS        | Mr Jones     |
| 1001           | Maths            | EdExcel    | Ms Parker    |
| 1001           | Physics          | OCR        | Mr Peters    |
| 1002           | Maths            | AQA        | Ms Parker    |
| 1002           | Biology          | WJEC       | Mrs Patel    |
| 1002           | Music            | AQA        | Ms Daniels   |
| 1003           | Computer Science | BCS        | Mr Jones     |
| 1003           | Maths            | EdExcel    | Ms Parker    |
| 1003           | Physics          | OCR        | Mr Peters    |
| 1004           | Maths            | AQA        | Ms Parker    |
| 1004           | Physics          | OCR        | Mr Peters    |
| 1004           | Biology          | WJEC       | Mrs Patel    |
| 1005           | Computer Science | BCS        | Mr Jones     |
| 1005           | Maths            | EdExcel    | Ms Parker    |
| 1005           | Music            | AQA        | Ms Daniels   |

---

## 3NF - Third Normal Form
In 3NF, transitive dependencies were removed by separating the `Teacher Name` into a new table linked to the `Course Name`.

### Courses Table
| Course Name      | Exam Board |
|------------------|------------|
| Computer Science | BCS        |
| Maths            | EdExcel    |
| Physics          | OCR        |
| Biology          | WJEC       |
| Music            | AQA        |

### Teachers Table
| Course Name      | Teacher Name |
|------------------|--------------|
| Computer Science | Mr Jones     |
| Maths            | Ms Parker    |
| Physics          | Mr Peters    |
| Biology          | Mrs Patel    |
| Music            | Ms Daniels   |

### Student_Courses Table (Final)
| Student Number | Course Name      |
|----------------|------------------|
| 1001           | Computer Science |
| 1001           | Maths            |
| 1001           | Physics          |
| 1002           | Maths            |
| 1002           | Biology          |
| 1002           | Music            |
| 1003           | Computer Science |
| 1003           | Maths            |
| 1003           | Physics          |
| 1004           | Maths            |
| 1004           | Physics          |
| 1004           | Biology          |
| 1005           | Computer Science |
| 1005           | Maths            |
| 1005           | Music            |

---

## References

Brumm, B. (2023) *Normalization in SQL DBMS: 1NF, 2NF, 3NF, and BCNF Examples*. POPSQL, 26 July. Available at: [https://popsql.com/blog/normalization-in-sql](https://popsql.com/blog/normalization-in-sql) (Accessed: 24 October 2024).
