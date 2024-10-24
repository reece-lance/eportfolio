# Relational Database Task

---

## Task Description

This task involved building a relational database system using SQLite. The data, previously normalised to 3rd Normal Form (3NF) and stored in CSV files, covered students, courses, exam boards, and teachers. The goal was to implement primary and foreign keys and ensure referential integrity, specifically testing cascading deletes. Key steps included defining the tables, importing the existing CSV files, and validating referential integrity through deletion tests.

---

## Steps Completed

1. **Database and Table Creation**  
   - Created tables for `Students`, `Courses`, `Teachers`, and `Student_Courses`, ensuring correct foreign key relationships.

2. **Data Importing**  
   - Imported previously created CSV files (from the normalisation task) into the database using Pandas.

3. **Referential Integrity Testing**  
   - Deleted student `1001` and verified that related records in `Student_Courses` were deleted due to the `ON DELETE CASCADE` rule.

---

## Feedback Received

- **Positive**: Efficient data import and proper use of foreign key constraints with cascading deletes.
- **Improvement Suggestion**: Consider adding indexing for better performance with larger datasets.

Here is the [Full Code](./data-build.py).

Here is the [Database](./student_course_database.db).

---

## References
Brumm, B. (2023) *Normalization in SQL DBMS: 1NF, 2NF, 3NF, and BCNF Examples*. POPSQL, 26 July. Available at: [https://popsql.com/blog/normalization-in-sql](https://popsql.com/blog/normalization-in-sql) (Accessed: 24 October 2024).
