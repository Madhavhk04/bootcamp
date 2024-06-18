import sqlite3
conn = sqlite3.connect('futurense.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

users_data = [
    ('arpita0507', 'password1', 'arpita@example.com', 'Arpita', 'M', 'student'),
    ('madhav99', 'password2', 'madhav@example.com', 'Madhav', 'H', 'student'),
    ('adwaid90', 'password3', 'adwaid@example.com', 'Adwaid', 'K', 'student'),
    ('prathmesh67', 'password4', 'prathmesh@example.com', 'Prathmesh', 'K', 'student'),
    ('gurkirat', 'password5', 'gurkirat@example.com', 'Gurkirat', 'S', 'student'),
    ('harsha', 'password6', 'harsha@example.com', 'Harshvardhan', 'R', 'student'),
    ('rajiv_mehta', 'hashed_password7', 'rajiv.mehta@example.com', 'Rajiv', 'Mehta', 'instructor'),
    ('priya_agrawal', 'hashed_password8', 'priya.agrawal@example.com', 'Priya', 'Agrawal', 'instructor'),
    ('vijay_patel', 'hashed_password9', 'vijay.patel@example.com', 'Vijay', 'Patel', 'admin'),
    ('sunita_rao', 'hashed_password10', 'sunita.rao@example.com', 'Sunita', 'Rao', 'admin')
]

for user in users_data:
    try:
        cursor.execute('''
        INSERT INTO User (username, password_hash, email, first_name, last_name, role)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', user)
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {user}: {e}")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name VARCHAR(100) NOT NULL,
    description TEXT,
    instructor_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (instructor_id) REFERENCES User(user_id)
)
''')

courses_data = [
    ('Data Communication and Computer Networks', 'Introduction to networking principles', 7),
    ('Data Structures & Algorithms', 'Comprehensive course on data structures and algorithms', 7),
    ('Database Design and Modelling (SQL)', 'Course on SQL and database design', 8),
    ('Artificial Intelligence Basics', 'Introduction to AI concepts', 8)
]

for course in courses_data:
    try:
        cursor.execute('''
        INSERT INTO Courses (course_name, description, instructor_id)
        VALUES (?, ?, ?)
        ''', course)
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {course}: {e}")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)
''')

enrollment_data = [
    (1, 1), (1, 2), (1, 3),
    (2, 1), (3, 2), (4, 3),
    (5, 1), (6, 4), (7, 2),
    (8, 3), (9, 1), (10, 4)
]

for enrollment in enrollment_data:
    try:
        cursor.execute('''
        INSERT INTO Enrollment (user_id, course_id)
        VALUES (?, ?)
        ''', enrollment)
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {enrollment}: {e}")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    due_date TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)
''')

assignments_data = [
    (1, 'Networking Assignment 1', 'Complete the given networking tasks', '2024-07-01'),
    (1, 'Networking Assignment 2', 'Complete the given tasks on OSI model', '2024-07-15'),
    (2, 'Data Structures Assignment 1', 'Implement data structures', '2024-07-01'),
    (2, 'Data Structures Assignment 2', 'Solve algorithm problems', '2024-07-15'),
    (3, 'SQL Assignment 1', 'Create SQL queries for the database', '2024-07-01'),
    (3, 'SQL Assignment 2', 'Design a database schema', '2024-07-15')
]

for assignment in assignments_data:
    try:
        cursor.execute('''
        INSERT INTO Assignments (course_id, title, description, due_date)
        VALUES (?, ?, ?, ?)
        ''', assignment)
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {assignment}: {e}")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Grades (
    grade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    course_id INTEGER,
    grade VARCHAR(10),
    graded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
)
''')

grades_data = [
    (1, 1, 'A', '2024-06-20'),
    (2, 1, 'B', '2024-06-22'),
    (3, 2, 'A', '2024-06-24'),
    (4, 2, 'B', '2024-06-26'),
    (5, 3, 'A', '2024-06-28'),
    (6, 3, 'B', '2024-06-30')
]

for grade in grades_data:
    try:
        cursor.execute('''
        INSERT INTO Grades (user_id, course_id, grade, graded_at)
        VALUES (?, ?, ?, ?)
        ''', grade)
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {grade}: {e}")

cursor.execute('''
CREATE TABLE IF NOT EXISTS Messages (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    sender_id INTEGER,
    receiver_id INTEGER,
    subject VARCHAR(100),
    content TEXT,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES User(user_id),
    FOREIGN KEY (receiver_id) REFERENCES User(user_id)
)
''')

messages_data = [
    (1, 7, 'Question about networking', 'I have a question about the OSI model.', '2024-06-10 10:00:00'),
    (2, 8, 'Help with SQL', 'I need help with SQL queries.', '2024-06-11 11:00:00'),
    (3, 7, 'Doubt in data structures', 'I have a doubt in linked lists.', '2024-06-12 12:00:00'),
    (4, 8, 'Clarification needed', 'I need clarification on AI concepts.', '2024-06-13 13:00:00')
]

for message in messages_data:
    try:
        cursor.execute('''
        INSERT INTO Messages (sender_id, receiver_id, subject, content, sent_at)
        VALUES (?, ?, ?, ?, ?)
        ''', message)
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {message}: {e}")

conn.commit()
conn.close()
