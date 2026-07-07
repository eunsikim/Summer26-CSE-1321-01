def main():
    my_tuple_1 = (1, 2, 3)

    my_tuple_2 = (4, 5)

    print(f"my_tuple_1: {my_tuple_1}")
    print(f"my_tuple_2: {my_tuple_2}")

    my_tuple_2 += my_tuple_1

    my_tuple_2 += tuple([100])

    print(f"Combined: {my_tuple_2}")
    
if __name__ == "__main__":
    main()