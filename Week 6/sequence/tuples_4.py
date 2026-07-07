def average_calc(*grades):
    sum_grades = sum(grades)

    return sum_grades / len(grades)

def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    return name, age

def main():
    print(average_calc(100, 50, 100))

    b, a = get_user_info()

    print(f"{b} is {a} years old")

if __name__ == "__main__":
    main()