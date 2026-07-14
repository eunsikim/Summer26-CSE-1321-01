class Student:
    name = ""

class Classroom:
    list_of_students = []

    def print_students(self):
        for student in self.list_of_students:
            print(student.name, end =", ")
        print()

s1 = Student()
s1.name = "Alice"

s2 = Student()
s2.name = "Bob"

c1 = Classroom()
c1.list_of_students = []
c2 = Classroom()
c2.list_of_students = []

c1.list_of_students.append(s1)
c2.list_of_students.append(s2)

print("Classroom 1 classlist:")
c1.print_students()
print()
print("Classroom 2 classlist:")
c2.print_students()
