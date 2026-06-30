def get_average(grades:list):
    sum_grades = 0

    for grade in grades:
        sum_grades += grade
    
    average = sum_grades / len(grades)

    return average

def get_grade(grade_type:str):
    if grade_type == "quiz":
        quiz_grade = []

        for x in range(10):
            while True:
                grade = float(input(f"Input your {grade_type} {x + 1} grade: "))

                if grade < 0 or grade > 100:
                    print("Please enter a valid grade [0, 100]")
                else:
                    break
            quiz_grade.append(grade)
        
        return quiz_grade
            
    elif grade_type == "midterm" or grade_type == "final":
        while True:
            grade = float(input(f"Input your {grade_type} exam grade: "))

            if grade >= 0 and grade <= 100:
                return grade
            else:
                print("Please enter a valid grade [0, 100]")

def convert_to_letter_grade(grade:float):
    if grade >= 89.5:
        return "A"
    elif grade >= 79.5:
        return "B"
    elif grade >= 69.5:
        return "C"
    elif grade >= 59.5:
        return "D"
    else:
        return "F"

# [100, 100]
def calculate_final_grade(quizzes:list, midterm:float, final:float):
    # Applying the Quiz policy
    lowest_quiz = 100.0

    for grade in quizzes:
        if grade < lowest_quiz:
            lowest_quiz = grade
    
    quizzes.remove(lowest_quiz)

    quiz_average = get_average(quizzes)

    # Final
    if final > midterm:
        midterm = final

    final_grade = quiz_average * .3 + midterm * .3 + final * .4

    return final_grade


def main():
    quizzes = get_grade("quiz")
    midterm = get_grade("midterm")
    final = get_grade("final")

    final_grade = calculate_final_grade(quizzes, midterm, final)

    final_grade_letter = convert_to_letter_grade(final_grade)

    print(f"Final grade: {final_grade_letter}")

if __name__ == "__main__":
    main()