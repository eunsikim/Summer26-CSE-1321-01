def main():
    numbers = [5, 4, 3, 6, 2]

    print(numbers)

    for i in range(len(numbers)):
        for y in range(len(numbers) - i - 1):
            if numbers[y] > numbers[y + 1]:
                # swap
                temp = numbers[y]
                numbers[y] = numbers[y + 1]
                numbers[y + 1] = temp 
        
    print(numbers)

if __name__ == "__main__":
    main()