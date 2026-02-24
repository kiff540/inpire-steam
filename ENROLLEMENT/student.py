class Student:
    def __init__(self, name, id_number, course):
        self.name = name
        self.id_number = id_number
        self.course = course

    def display_info(self):
        print(f"--- Enrollment Details ---")
        print(f"Name:    {self.name}")
        print(f"ID:      {self.id_number}")
        print(f"Course:  {self.course}")
        print("-" * 26)