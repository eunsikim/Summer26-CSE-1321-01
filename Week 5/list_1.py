def main():
    # Initialized a new empty list
    my_list = []

    students = ["Alice", "Bob", "Dave", "Charlie", "Bob"]

    print(f"my_list contents: {my_list}")

    # Adding things in a list
    my_list.append(10)
    my_list.append(50)
    my_list.append(100)

    print(f"my_list contents: {my_list}")

    # Accessing/Reading and iterating a list
    print("Printing each single student:")
    for name in students:
        print(name)
    
    print()

    print("Printing every other student:")
    # Instead of printing each single student
    # we want to print every other
    index = 0

    while index < len(students):
        if index % 2 == 0:
            print(students[index])

        index += 1

    # Updating/Reassigning values in a list
    students[2] = "David"
    print(f"Student names: {students}")

    print()

    index = 0
    print("Choose a name by its index:")
    for name in students:
        print(f"{index} - {name}")
        index += 1

    selection = int(input("Enter index: "))

    new_name = input("Enter a name: ")

    students[selection] = new_name
    print(f"Student names: {students}")

    # Removing elements in a list
    # Removing the first occurence of an element
    students.remove("Bob")
    print(f"Student names: {students}")
    print(students[1])

    # Removing by Index (pop())
    print("Popping index 0")
    last_deleted_name = students.pop(0)
    print(f"{last_deleted_name} was deleted from the list")
    print(f"Student names: {students}")

    print()
    # Removing by Index (del statement)
    del students[1]
    print(f"Student names: {students}")

    # Remove everything in a list
    print("Clearing list...")
    students.clear()
    print(f"Student names: {students}")
    
if __name__ == "__main__":
    main()