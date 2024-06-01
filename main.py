from database.Student import Student
from database.database import Database

db = Database('school.db')

student_manager = Student(db)

# Додавання студента
student_manager.add_student('John Doe', 20, 1)

# Отримання студента
student = student_manager.get_student(1)
print(student)

# Оновлення студента
student_manager.update_student(1, age=21)

# Видалення студента
student_manager.delete_student(1)
