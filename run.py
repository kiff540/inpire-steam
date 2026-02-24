# enrollment_manager.py
from students import Student

def register_student():
    print("Enter Student Details")
    name = input("Name: ")
    id_num = input("ID Number: ")
    course = input("Course: ")
    
    # Create an instance of the Student class
    new_student = Student(name, id_num, course)
    return new_student