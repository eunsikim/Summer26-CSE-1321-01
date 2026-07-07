def main():
    list_of_list = [
            [1, 2, 3], 
            [4, 5, 6], 
            [7, [8.1, 8.2, 8.3], 9]
        ]

    # The more list we nest, we add another set of `[]` per
    # nesting level
    print(list_of_list[2][1][0])

    
if __name__ == "__main__":
    main()