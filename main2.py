import sqlite3

def create_tables():
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL
    )
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        instructor TEXT NOT NULL
    )''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS student_courses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(course_id) REFERENCES courses(id),
    PRIMARY KEY(student_id, course_id)
    )
    '''
    )
    con.commit()
    con.close()


def add_student(name, age, major):
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute('INSERT INTO students (name, age, major) VALUES (?, ?, ?)', (name, age, major))
    con.commit()
    con.close()

def add_course(course_name, instructor):
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute('INSERT INTO courses (course_name, instructor) VALUES (?, ?)', (course_name, instructor))


def register_student_to_course(student_id, course_id):
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute('INSERT INTO students_courses (student_id, course_id) VALUES (?, ?)', (student_id, course_id))
    con.commit()
    con.close()

def view_students():
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM courses')
    courses = cur.fetchall()
    con.close()
    return courses

def view_courses():
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM courses')
    courses = cur.fetchall()
    con.close()
    return courses

def view_students_in_course(course_id):
    con = sqlite3.connect('E:\db2\daa.db')
    cur = con.cursor()
    cur.execute(
        '''
        SELECT students.id, students.name, students.age, students.major
        FROM students
        JOIN student_courses ON students.id = student_courses.student_id
        WHERE student_courses.course_id = ?
        ''', (course_id,))
    students = cur.fetchall()
    con.close()
    return students

def main():
    create_tables()

    while True:
        print("\n1. Додати нового студента")
        print("2. Додати новий курс")
        print("3. Показати список студентів")
        print("4. Показати список курсів")
        print("5. Зареєструвати студента на курс")
        print("6. Показати студентів на конкретному курсі")
        print("7. Вийти")

        choice = input("Оберіть опцію (1-7): ")

        if choice == "1":
            name = input("Уведи ім'я тих студентів: ")
            age = int(input("Уведи вік тих студентів: "))
            major = input("Уведи студентів major: ")
            add_student(name, age, major)

        elif choice == "2":
            course_name = input("Уведи course ім'я: ")
            instructor = input("Уведи course instructor: ")
            add_course(course_name, instructor)

        elif choice == "3":
            student_id = str(input("Уведи id студента: "))
            course_id = int(input("Уведи id course: "))
            register_student_to_course(student_id, course_id)

        elif choice == "4":
            students = view_students()
            for student in students:
                print(student)

        elif choice == "5":
            courses = view_courses()
            for course in courses:
                print(course)



        elif choice == "6":
            course_id = int(input("Уведи id course: "))
            students = view_students_in_course(course_id)
            for student in students:
                print(student)

        elif choice == "7":
            break

        else:
            print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")

if __name__ == '__main__':
    main()