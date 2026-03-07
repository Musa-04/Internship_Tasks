-- =========================================
-- ER MODEL IMPLEMENTATION USING SQL
-- Student Course Enrollment System
-- =========================================

-- 1. Create Database
CREATE DATABASE student_management;

-- 2. Use Database
USE student_management;

-- =========================================
-- TABLE 1: STUDENT (Entity)
-- =========================================

CREATE TABLE student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);

-- =========================================
-- TABLE 2: INSTRUCTOR (Entity)
-- =========================================

CREATE TABLE instructor (
    instructor_id INT PRIMARY KEY,
    instructor_name VARCHAR(50),
    department VARCHAR(50)
);

-- =========================================
-- TABLE 3: COURSE (Entity)
-- =========================================

CREATE TABLE course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    credits INT,
    instructor_id INT,
    
    FOREIGN KEY (instructor_id) REFERENCES instructor(instructor_id)
);

-- =========================================
-- TABLE 4: ENROLLMENT (Relationship)
-- Many-to-Many relationship between
-- Student and Course
-- =========================================

CREATE TABLE enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES course(course_id)
);

-- =========================================
-- INSERT SAMPLE DATA
-- =========================================

INSERT INTO student VALUES
(1,'Arun',20,'Computer Science'),
(2,'Rahul',21,'Electronics'),
(3,'Sneha',19,'Mechanical');

INSERT INTO instructor VALUES
(101,'Dr. Sharma','Computer Science'),
(102,'Dr. Mehta','Electronics');

INSERT INTO course VALUES
(201,'Database Systems',4,101),
(202,'Digital Electronics',3,102);

INSERT INTO enrollment(student_id,course_id) VALUES
(1,201),
(2,202),
(3,201);

-- =========================================
-- SAMPLE QUERIES
-- =========================================

-- View Students
SELECT * FROM student;

-- View Courses
SELECT * FROM course;

-- View Enrollment Details
SELECT 
student.student_name,
course.course_name
FROM enrollment
JOIN student ON enrollment.student_id = student.student_id
JOIN course ON enrollment.course_id = course.course_id;