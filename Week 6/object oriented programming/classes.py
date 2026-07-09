class Student:
    # Constructor Function
    def __init__(self, _name, _courses):
        print("Contstructing a Student type object...")
        # Define OBJECT/INSTANCE attributes
        self.name = _name
        self.courses = _courses
        self.GPA = 0.0

    def print_student_info(self):
        print(f"{self.name}, Courses: {self.courses}, GPA: {self.GPA}")

def main():
    s1 = Student("Alice", ["CSE 1321", "CSE 1321L"])
    s2 = Student("Bob", ["CSE 1321"])

    s1.print_student_info()
    s2.print_student_info()

    s1.name = "Dave"
    s1.print_student_info()
    s2.print_student_info()

if __name__ == "__main__":
    main()