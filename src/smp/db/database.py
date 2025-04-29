import sqlite3
from app.role import RoleName


def create_database(db_name):
    """
    Create a SQLite database with predefined schema for a school management system.

    This function establishes a database connection and creates tables for:
    - Roles
    - Users
    - Classrooms
    - Subjects
    - Teachers
    - Students
    - Exams
    - Grades
    - Attendance
    - Timetables

    The function also inserts a default admin role and user for initial system setup.

    Args:
        db_name (str): The filename/path for the SQLite database to be created.
    """
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create tables
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Role (
        role_id INTEGER PRIMARY KEY AUTOINCREMENT,
        role_name TEXT NOT NULL UNIQUE
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS User (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role_id INTEGER NOT NULL,
        recorded_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (role_id) REFERENCES Role(role_id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Classroom (
        classroom_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        division INTEGER,
        capacity INTEGER
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Subject (
        subject_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        teacher_id INTEGER NOT NULL,
        class_id INTEGER NOT NULL,
        description TEXT,
        FOREIGN KEY (teacher_id) REFERENCES Teacher(teacher_id)
        FOREIGN KEY (class_id) REFERENCES Classroom(classroom_id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Teacher (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        mother TEXT NOT NULL,
        gender TEXT CHECK(gender IN ('male', 'female')) NOT NULL,
        public_number TEXT UNIQUE,
        date_of_birth DATE,
        address TEXT,
        phone TEXT,
        email TEXT
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Student (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        class_id INTEGER,
        full_name TEXT NOT NULL,
        mother TEXT NOT NULL,
        gender TEXT CHECK(gender IN ('male', 'female')) NOT NULL,
        public_number TEXT UNIQUE,
        date_of_birth DATE,
        address TEXT,
        phone TEXT,
        FOREIGN KEY (class_id) REFERENCES Classroom(classroom_id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Exam (
        exam_id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT CHECK(type IN ('midterm', 'final', 'quiz')) NOT NULL,
        subject_id INTEGER NOT NULL,
        class_id INTEGER NOT NULL,
        exam_date DATE NOT NULL,
        description TEXT,
        FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Grade (
        grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        exam_id INTEGER NOT NULL,
        score FLOAT NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Student(student_id),
        FOREIGN KEY (exam_id) REFERENCES Exam(exam_id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Attendance (
        attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER NOT NULL,
        date DATE NOT NULL,
        status TEXT CHECK(status IN ('Present', 'Absent', 'Late', 'Excused')) NOT NULL,
        FOREIGN KEY (student_id) REFERENCES Student(student_id)
    );
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Timetable (
        timetable_id INTEGER PRIMARY KEY AUTOINCREMENT,
        classroom_id INTEGER NOT NULL,
        subject_id INTEGER NOT NULL,
        day_of_week TEXT CHECK(day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')),
        start_time TIME NOT NULL,
        end_time TIME NOT NULL,
        FOREIGN KEY (classroom_id) REFERENCES Classroom(classroom_id),
        FOREIGN KEY (subject_id) REFERENCES Subject(subject_id)
    );
    """
    )

    cursor.execute("INSERT INTO Role (role_name) VALUES (?) ", (RoleName.ADMIN.value,))
    cursor.execute(
        "INSERT INTO User (full_name,username,password,role_id) VALUES (?,?,?,?)",
        ("Admin-Dev", "dev", "123", 1),
    )

    conn.commit()
    conn.close()
