def read_input(students):
    id_counter = 1

    while True:
        info = input("> ")

        if info == "-1":
            return
        else:
            info = info.split(",")

            student = {
                "firstName": info[0],
                "quizzes": [float(x) for x in info[1:10]],
                "midterm_exam": float(info[11]),
                "final_exam": float(info[12])
            }

            students[id_counter] = student

            id_counter += 1

def avg_calc(grades):
    return sum(grades)/len(grades)

def main():
    students = {}

    class_quiz_avg = []

    read_input(students)

    for student in students.values():
        student_quiz_avg = avg_calc(student["quizzes"])

        print(f"{student["firstName"]} has an avg. Quiz grade of {student_quiz_avg:.2f}")

        class_quiz_avg.append(student_quiz_avg)
    
    print(f"Class Quiz Average: {avg_calc(class_quiz_avg):.2f}")

if __name__ == "__main__":
    main()