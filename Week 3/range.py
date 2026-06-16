def main():
    # 3 (Stop) is exclusive
    for x in range(3): #It generates the sequence: 0, 1, 2
        print(x)

    print()

    # 5 (start) is inclusive and 8 (stop) is exclusive
    for x in range(5, 8):
        print(x)
    
    print()

    # The third (step) value indicates the interval between each number in the sequence
    for x in range(1, 11, 2):
        print(x)

if __name__ == "__main__":
    main()