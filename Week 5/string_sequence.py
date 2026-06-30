def main():
    my_string = "hello"

    print("Printing my_string with a FOR loop")
    for character in my_string:
        print(character)

    print()

    print("Printing my_string with a WHILE loop")
    index = 0

    while index < len(my_string):
        print(my_string[index])
        index += 1


    
if __name__ == "__main__":
    main()