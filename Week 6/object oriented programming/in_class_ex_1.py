class Course:
    def __init__(self, name, grading_scheme):
        # self.credits
        self.name = name
        # self.location
        # self.time
        # self.CRN
        # self.capacity
        # self.syllabus
        # self.instructor

        # List of Student type objects
        self.students = []

        self.grading_scheme = grading_scheme
    
    def calculate_final_grade(self):
        for student in self.students:
            grade = 0
            current_index = 0
            dist_index = 0

            for grading_item in self.grading_scheme:
                if grading_item == "dist":
                    break

                if self.grading_scheme[grading_item] > 1:
                    grade += self.calc_avg(student.courses[self][current_index : current_index + self.grading_scheme[grading_item] - 1]) * self.grading_scheme["dist"][dist_index] / 100

                    current_index += self.grading_scheme[grading_item]

                    dist_index += 1
                
                else:
                    grade += student.courses[self][current_index] * self.grading_scheme["dist"][dist_index] / 100

                    current_index += self.grading_scheme[grading_item] 
                    dist_index += 1
        
            print(grade)

    def calc_avg(self, grades):
        return sum(grades) / len(grades)

    def print_classlist(self):
        print(f"{self.name} Classlist")

        for student in self.students:
            print(student.name)
            print(student.courses[self])

class Student:
    # Constructor Function
    def __init__(self, _name, _courses):
        print("Contstructing a Student type object...")
        # Define OBJECT/INSTANCE attributes
        self.name = _name
        # courses will be a dictionary
        # key: Course object, Value: list of grades
        # {cse1321:[80, 97, 82, ...]}
        self.courses = _courses
        self.GPA = 0.0

    def print_student_info(self):
        print(f"{self.name}, Courses: {self.courses}, GPA: {self.GPA}")
    
    
        

def main():
    cse1321 = Course("CSE 1321", {
        "quizzes": 10,
        "midterm": 1,
        "final": 1,
        "dist": [30, 30, 40] 
    })

    cse1321L = Course("CSE 1321L", {
        "labs": 13,
        "assignments": 7,
        "midterm": 1,
        "final": 1,
        "dist": [10, 40, 20, 30]
    })

    s1 = Student("Alice", {
        cse1321:[88, 79, 64, 54, 90, 61, 62, 77, 87, 78, 76, 85],
        cse1321L:[79, 80, 80, 97, 84, 73, 97, 58, 71, 66, 74, 72, 76, 83, 75, 51, 62, 59, 68, 96, 60, 69]
    })

    s2 = Student("Bob", {
        cse1321:[73, 86, 73, 55, 100, 88, 76, 83, 51, 98, 75, 73]
    })

    cse1321.students.append(s1)
    cse1321L.students.append(s1)

    cse1321.students.append(s2)

    cse1321.print_classlist()
    cse1321L.print_classlist()

    cse1321.calculate_final_grade()

if __name__ == "__main__":
    main()