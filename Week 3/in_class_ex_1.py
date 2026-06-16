def main():
    my_string = "HelloWorld"

    counter = 0

    for character in my_string:
        if character.isupper() and counter != 0:
            print(" ", end="")

        print(character, end="")
        counter += 1

if __name__ == "__main__":
    main()