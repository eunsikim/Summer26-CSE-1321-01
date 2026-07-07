from in_exercise_1 import get_average

def main():
    classlist = []

    for i in range(3):
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        q1 = float(input("Enter Q1 Grade: "))
        q2 = float(input("Enter Q2 Grade: "))
        q3 = float(input("Enter Q3 Grade: "))

        classlist.append( [first_name, last_name, [q1, q2, q3]] )
        print()

    for i in range(len(classlist)):
        student_1 = get_average(classlist[i][2])
        print(f"{classlist[i][0]} {classlist[i][1]} has a Quiz Avg. of {student_1}")
        print()

    # Since classlist[x][2] references a list, we can also call any list function
    classlist[0][2].append(90)
    classlist[1][2].append(87)
    classlist[2][2].append(10)

    for i in range(len(classlist)):
        print(f"{classlist[i][0]} {classlist[i][2]}")
        print()

if __name__ == "__main__":
    main()