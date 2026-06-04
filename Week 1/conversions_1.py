def main():
    another_number = "10.0" # This will crash
    # another_number = 10.0 # This will not crash
    print(type(another_number))
    number = int(another_number)

    print(number)
    print(type(number))

if __name__ == "__main__":
    main()