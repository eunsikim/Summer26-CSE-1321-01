# As you may have heard, beginning Fall 2026, the requirement to 
# take CSE 1322 and CSE 1322L changed.

# You now need to pass BOTH CSE 1321 and CSE 1321L with a minimum grade of C to take it.
# Previous semesters you had to pass with a B.

# Imagine you took both CSE 1321 and CSE 1321L in Spring 2026 and now you are trying to register
# for CSE 1322 and CSE 1322L either on Summer 2026 or Fall 2026.

# Create a program that asks the user:
# - The letter grade they had for CSE 1321
# - The letter grade they had for CSE 1321L
# - What semester they are trying to register for CSE 1322 and CSE 1322L
# The program should tell the user if they match the pre-requisite

def main():
    grade_1321 = input("Enter your grade for CSE 1321: ")
    grade_1321Lab = input("Enter your grade for CSE 1321L: ")
    semester_applying = input("What semester do you want to register for CSE 1322 and CSE 1322L: ")

    if semester_applying == "fall 2026":
        if grade_1321 == "A" or grade_1321 == "B" or grade_1321 == "C":
            if grade_1321Lab == "A" or grade_1321Lab == "B" or grade_1321Lab == "C":
                print("You are good to register for CSE 1322 and CSE 1322L")
            else:
                print("You are not good to register for CSE 1322 and CSE 1322L")
        else:
            print("You are not good to register for CSE 1322 and CSE 1322L")

    elif semester_applying == "summer 2026":
        if grade_1321 == "A" or grade_1321 == "B":
            if grade_1321Lab == "A" or grade_1321Lab == "B":
                print("You are good to register for CSE 1322 and CSE 1322L")
            else:
                print("You are not good to register for CSE 1322 and CSE 1322L")
        else:
            print("You are not good to register for CSE 1322 and CSE 1322L")

if __name__ == "__main__":
    main()