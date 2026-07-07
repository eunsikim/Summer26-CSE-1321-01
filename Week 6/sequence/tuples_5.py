def main():
    my_tuple = (6, 3, 8, 2)

    numbers = list(my_tuple)

    print(numbers)

    for i in range(len(numbers)):
        for y in range(len(numbers) - i - 1):
            if numbers[y] > numbers[y + 1]:
                # swap
                temp = numbers[y]
                numbers[y] = numbers[y + 1]
                numbers[y + 1] = temp 
        
    print(numbers)

    my_tuple = tuple(numbers)

    print(my_tuple)
    print(type(my_tuple))

if __name__ == "__main__":
    main()