def main():
    shape = input("Enter a shape: ")

    match shape:
        case "square":
            print("You inserted a square.")
        case "triangle":
            print("You inserted a triangle.")
        case _:
            print("I do not know that shape.")
    
    print("[Program Terminated]")


if __name__ == "__main__":
    main()