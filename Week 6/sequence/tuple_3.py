def main():
    my_tuple = tuple(range(10))

    print("Iterating by Element (for each...)")
    for element in my_tuple:
        print(element)

    print()

    print("Iterating by Index")
    for index in range(len(my_tuple)):
        print(my_tuple[index])
    
if __name__ == "__main__":
    main()