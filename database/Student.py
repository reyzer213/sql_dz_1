
class Student:
    def __init__(self, db):
        self.db = db

    def add_student(self, name, age, course_id=None):
        self.db.execute_query('''
        INSERT INTO students (name, age, course_id) VALUES (?, ?, ?)
        ''', (name, age, course_id))

    def get_student(self, student_id):
        return self.db.fetch_one('''
        SELECT * FROM students WHERE id=?
        ''', (student_id,))

    def update_student(self, student_id, name=None, age=None, course_id=None):
        if name:
            self.db.execute_query('''
            UPDATE students SET name=? WHERE id=?
            ''', (name, student_id))
        if age:
            self.db.execute_query('''
            UPDATE students SET age=? WHERE id=?
            ''', (age, student_id))
        if course_id:
            self.db.execute_query('''
            UPDATE students SET course_id=? WHERE id=?
            ''', (course_id, student_id))

    def delete_student(self, student_id):
        self.db.execute_query('''
        DELETE FROM students WHERE id=?
        ''', (student_id,))
