# main.py
# main.py
from enrollment_manager import register_student

def main():
    # 1. Enroll the student initially
    student_1 = register_student()
    student_1.display_info()

    # 2. Ask to alter the course
    change = input("Do you want to change the course? (yes/no): ").lower()
    
    if change == 'yes':
        new_course_name = input("Enter the new course name: ")
        # Call the method we created in student.py
        student_1.update_course(new_course_name)
        
        # Show updated info
        print("\nUpdate Successful!")
        student_1.display_info()
    else:
        print("No changes made.")

if __name__ == "__main__":
    main()