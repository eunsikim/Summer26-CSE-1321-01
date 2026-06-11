# What is the output value printed?
def main():
    x = 10

    some_variable = 10

    match some_variable:
        case "10":
            x += 3
        case 10:
            x = 3
        case 10.0:
            x = x / 3
    
    print(x)

if __name__ == "__main__":
    main()